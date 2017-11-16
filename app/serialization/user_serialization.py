from flask_restful import Resource, reqparse, fields, marshal_with
from flask import g


class GetToken(fields.Raw):
    def output(self, key, obj):
        token = g.user.generate_auth_token()
        return token.decode('ascii')

user_fields = {
    'status': fields.String,
    'message': fields.String,
    'data': {
        'id': fields.Integer,
        'name': fields.String,
        'email': fields.String,
        'remember_token': fields.String,
        'created_at': fields.String,
        'updated_at': fields.String
    }
}