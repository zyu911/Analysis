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


class Users(Resource):
    @marshal_with(user_fields, envelope='data')
    def post(self):
        args = user_form.parse_args()
        if args['username'] is None or args['password'] is None:
            abort(400)  # missing arguments
        if User.query.filter_by(username=args['username']).first() is not None:
            abort(400)  # existing user
        user = User(username=args['username'])
        user.hash_password(args['password'])
        db.session.add(user)
        db.session.commit()
        g.user = user
        return user

    @auth.login_required
    @marshal_with(user_fields, envelope='data')
    def get(self):
        user = User.query.filter_by(id=1).first()
        print(user.__dict__)
        return user

