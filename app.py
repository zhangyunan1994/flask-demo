from flask import Flask, session, render_template, request, abort
from flask_cors import *

from config import *
from exts.exts import db
from models.models import User
from views.user_manager import user_manager

database_config = get_database_info("dev")
server_info = get_server_info()

app = Flask(__name__)
CORS(app, supports_credentials=True)

app.secret_key = b'_5#y2L"F4Q8z/'
app.config["SQLALCHEMY_DATABASE_URI"] = f'mysql+pymysql://{ database_config.User }:{database_config.Password}@{database_config.Host}:{database_config.Port}/{database_config.Name}'

app.register_blueprint(user_manager)

db.init_app(app)


@app.route('/')
def index():
    # render_template 为使用模板渲染对应的页面并跳转到页面，对应的页面在 templates 下面
    return render_template('index.html')


@app.route('/toLogin')
def login_layer():
    if 'current_user_id' in session:
        return render_template('app/index.html', nickname=session['current_user_nickname'])
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    param = request.get_json()
    user = User.query.filter_by(username=param['username']).filter(User.password == param['password']).first()
    status = 1
    message = ""
    if user:
        if user.status == 1:
            session['current_user_id'] = user.id
            session['current_user_nickname'] = user.nickname
        else:
            status = 403
            message = '用户已禁用'
    else:
        status = 404
        message = '用户名或者密码错误'
    return {
        'status': status,
        'message': message
    }


@app.route('/logout')
def logout():
    if 'current_user_id' in session:
        session.clear()
    return render_template('index.html')


@app.route('/app/index')
def app_index_layer():
    if 'current_user_id' in session:
        return render_template('app/index.html', nickname=session['current_user_nickname'])
    return render_template('login.html')


@app.before_request
def before_user():
    if request.path in ['/', '/toLogin', '/login']:
        return
    if 'current_user_id' not in session:
        abort(401)


if __name__ == '__main__':
    app.run(port=11000, debug=True)
