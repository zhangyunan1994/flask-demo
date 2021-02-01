from flask import Blueprint

user_manager = Blueprint("movie", __name__, url_prefix='/app/movie')
