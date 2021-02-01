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