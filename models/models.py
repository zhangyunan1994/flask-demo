from marshmallow import Schema, fields

from exts.APIException import APIException
from exts.DictUtil import remove_none_key
from exts.exts import db


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    status = db.Column(db.Integer)
    create_time = db.Column(db.DateTime, nullable=False)

    def add(self):
        db.session.add(self)
        db.session.commit()

    def modify(self):
        u = User.query.filter(User.id == self.id).first()
        if not u:
            raise APIException(500, "用户不存在")
        user_schema = UserSchema()
        data = user_schema.dump(self)
        remove_none_key(data)
        db.session.query(User).filter(User.id == self.id).update(data)
        db.session.commit()


class UserSchema(Schema):
    id = fields.Int()
    username = fields.Str()
    password = fields.Str()
    nickname = fields.Str()
    status = fields.Int()
    create_time = fields.DateTime()


class MovieCategory(db.Model):
    __tablename__ = 'movie_category'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    create_time = db.Column(db.DateTime, nullable=False)

    def add(self):
        db.session.add(self)
        db.session.commit()

    def modify(self):
        u = MovieCategory.query.filter(MovieCategory.id == self.id).first()
        if not u:
            raise APIException(500, "分类不存在")
        schema = MovieCategorySchema()
        data = schema.dump(self)
        remove_none_key(data)
        db.session.query(MovieCategory).filter(MovieCategory.id == self.id).update(data)
        db.session.commit()

    def delete(self):
        category = MovieCategory.query.filter(MovieCategory.id == self.id).first()
        if not category:
            # 用户已经存在，不能添加
            raise APIException(500, "分类不存在")
        db.session.delete(category)
        db.session.commit()


class MovieCategorySchema(Schema):
    id = fields.Int()
    name = fields.Str()
    create_time = fields.DateTime()


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer)
    img_url = db.Column(db.String)
    description = db.Column(db.String)
    douban_score = db.Column(db.Float)
    release_time = db.Column(db.DateTime)
    resource_url = db.Column(db.String)
    name = db.Column(db.String, nullable=False)
    create_time = db.Column(db.DateTime, nullable=False)

    def add(self):
        db.session.add(self)
        db.session.commit()

    def modify(self):
        schema = MovieSchema()
        data = schema.dump(self)
        remove_none_key(data)
        db.session.query(Movie).filter(Movie.id == self.id).update(data)
        db.session.commit()


class MovieSchema(Schema):
    id = fields.Int()
    category_id = fields.Int()
    img_url = fields.Str()
    description = fields.Str()
    douban_score = fields.Float()
    release_time = fields.DateTime()
    resource_url = fields.Str()
    name = fields.Str()
    create_time = fields.DateTime()
