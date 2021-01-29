from flask import Flask, render_template
from flask_cors import *


app = Flask(__name__)
CORS(app, supports_credentials=True)


@app.route('/')
def index():
    # render_template 为使用模板渲染对应的页面并跳转到页面，对应的页面在 templates 下面
    return render_template('index.html')


@app.route('/login')
def login():
    # 此处应该判断一下，如果已经登录，就不要跳到登录页面了
    return render_template('login.html')


if __name__ == '__main__':
    app.run(port=11000, debug=True)
