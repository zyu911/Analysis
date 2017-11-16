# _*_ coding: utf-8 _*_
from flask_restful import Resource, reqparse, fields, marshal_with
from flask import request, abort, g, jsonify, url_for
from app.models.user import User
from functools import wraps
from app import db
from app.forms.user_form import user_form
from app.serialization.user_serialization import user_fields
from runserver import auth


@auth.verify_password
def verify_password(username_or_token, password):
    user = User.query.filter_by(remember_token=username_or_token).first()
    if not user:
        user = User.query.filter_by(email=username_or_token).first()
        if not user or not user.verify_password(password):
            return False
    g.user = user
    return True


@auth.error_handler
def error_handler():
    abort(401)
    # return jsonify({'status': False, 'message': u'用户名或密码错误!', 'data': {}})


class Register(Resource):
    @marshal_with(user_fields, envelope='data')
    def post(self):
        args = user_form.parse_args(strict=True)
        print(args)
        if User.query.filter_by(email=args['email']).first() is not None:
            abort(400)  # existing user
        user = User(email=args['email'])
        user.hash_password(args['password'])
        db.session.add(user)
        db.session.commit()
        g.user = user
        return user


class Login(Resource):
    @auth.login_required
    @marshal_with(user_fields)
    def post(self):
        user = g.user
        setattr(user, 'status', True)
        setattr(user, 'message', u'登录成功!')
        return user, 200
