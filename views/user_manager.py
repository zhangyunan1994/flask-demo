import datetime

from flask import Blueprint, request, jsonify, render_template
from sqlalchemy import or_

from exts.APIException import APIException
from models.models import User, UserSchema

user_manager = Blueprint("user_manager", __name__, url_prefix='/app/user')


@user_manager.route("index")
def index():
    return render_template('app/user/index.html')


@user_manager.route("/detail/<int:id>", methods=['GET'])
def detail(id: int):
    user = User.query.filter(User.id == id).first()

    user_schema = UserSchema()
    data = user_schema.dump(user)
    return jsonify(data)


@user_manager.route("list", methods=['GET'])
def search():
    filter_text = request.args.get("filterText")
    if filter_text:
        result = User.query.filter(or_(User.nickname.like(filter_text), User.username.like(filter_text))).all()
    else:
        result = User.query.all()
    user_schema = UserSchema(many=True)
    data = user_schema.dump(result)
    return jsonify(data)


@user_manager.route("add", methods=['POST'])
def add():
    user_info = request.get_json()
    user = User.query.filter_by(username=user_info['username']).first()
    if user:
        # 用户已经存在，不能添加
        raise APIException(500, "用户已经存在")
    user = User()
    user.nickname = user_info['nickname']
    user.username = user_info['username']
    user.password = user_info['password']
    user.create_time = datetime.datetime.now()
    user.status = 1
    user.add()
    return {"code": 200}


@user_manager.route("modify", methods=['POST'])
def modify():
    user_info = request.get_json()
    user = User.query.filter_by(username=user_info['username']).first()
    if user and user.id != user_info['id']:
        # 用户已经存在，不能添加
        raise APIException(500, "用户已经存在")
    user = User()
    user.nickname = user_info['nickname']
    user.username = user_info['username']
    user.password = user_info['password']
    user.status = user_info['status']
    user.id = user_info['id']
    user.modify()
    return {"code": 200}

