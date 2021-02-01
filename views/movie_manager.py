import datetime

from flask import Blueprint, render_template, request, jsonify

from exts.APIException import APIException
from models.models import MovieCategory, MovieCategorySchema

movie_manager = Blueprint("movie", __name__, url_prefix='/app/movie')


@movie_manager.route("/category/index")
def category_index():
    return render_template('app/movie/category.html')


@movie_manager.route("/category/list", methods=['GET'])
def search_category():
    filter_text = request.args.get("filterText")
    if filter_text:
        result = MovieCategory.query.filter(MovieCategory.name.like(filter_text)).all()
    else:
        result = MovieCategory.query.all()
    schema = MovieCategorySchema(many=True)
    data = schema.dump(result)
    return jsonify(data)


@movie_manager.route("/category/add", methods=['POST'])
def add_category():
    category_info = request.get_json()
    category = MovieCategory.query.filter(MovieCategory.name == category_info['name']).first()
    if category:
        # 用户已经存在，不能添加
        raise APIException(500, "分类已经存在")
    category = MovieCategory()
    category.name = category_info['name']
    category.create_time = datetime.datetime.now()
    category.add()
    return {"code": 200}


@movie_manager.route("/category/modify", methods=['POST'])
def modify_category():
    category_info = request.get_json()
    category = MovieCategory.query.filter(MovieCategory.name == category_info['name']).first()
    if category and category.id != category_info['id']:
        # 用户已经存在，不能添加
        raise APIException(500, "分类已经存在")
    category = MovieCategory()
    category.name = category_info['name']
    category.id = category_info['id']
    category.modify()
    return {"code": 200}


@movie_manager.route("/category/delete/<int:id>", methods=['DELETE'])
def delete_category(id):
    category = MovieCategory()
    category.id = id
    category.delete()
    return {"code": 200}


@movie_manager.route("/movie/index")
def index():
    return render_template('app/movie/movie.html')
