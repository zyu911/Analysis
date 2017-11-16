# _*_ coding: utf-8 _*_
from flask_restful import Resource, reqparse, fields, marshal_with
# from flask import request, abort, g, jsonify, url_for
# from app.models.user import User
# from flask.ext.httpauth import HTTPBasicAuth
# from functools import wraps
# from app import db
from app.forms.user_form import user_form
from app.serialization.user_serialization import user_fields
from app.serialization.histories_serialization import histories_fields
from app.models.histories import Histories
from runserver import auth
# from flask_restful.paging import retrieve_next_page


class HistoriesViews(Resource):
    @auth.login_required
    @marshal_with(histories_fields, envelope='data')
    def get(self, id=None):
        # args = user_form.parse_args()
        if not id:
            obj = Histories.query.all()
        else:
            obj = Histories.query.get(id)
        return obj

    def post(self):
        args = user_form.parse_args()
        return args