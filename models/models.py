from exts.exts import db
from marshmallow import Schema, fields


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    create_time = db.Column(db.DateTime, nullable=False)


class UserSchema(Schema):
    id = fields.Int()
    username = fields.Str()
    password = fields.Str()
    nickname = fields.Str()
    create_time = fields.DateTime()