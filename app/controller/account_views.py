# _*_ coding: utf-8 _*_
from flask_restful import Resource, reqparse, fields, marshal_with
from flask import request, abort, g, jsonify, url_for
from app.models.user import User
from functools import wraps
from app import db
from app.forms.user_form import user_form
from app import setting
from app.serialization.user_serialization import user_fields
from werkzeug.contrib.cache import SimpleCache
from runserver import auth
cache = SimpleCache()


@auth.verify_password
def verify_password(username_or_token, password):
    user = User.verify_auth_token(username_or_token)
    if user and not cache.has('user-%s' % user.id):
        return False
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


class Login(Resource):
    @auth.login_required
    @marshal_with(user_fields)
    def post(self):
        user = g.user
        token = user.generate_auth_token()
        cache.set('user-%s' % user.id, token, timeout=setting.TIMEOUT)
        setattr(user, 'status', True)
        setattr(user, 'remember_token', token)
        setattr(user, 'message', u'登录成功!')
        return user, 200


class Logout(Resource):
    @auth.login_required
    def get(self):
        cache.delete('user-%s' % g.user.id)
        return {'status': True, 'message': u'已退出登录', 'data': ''}
