from flask import Blueprint, request, jsonify, render_template
from sqlalchemy import or_

from models.models import User, UserSchema

user_manager = Blueprint("user_manager", __name__, url_prefix='/app/user')


@user_manager.route("index")
def index():
    return render_template('app/user/index.html')


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
