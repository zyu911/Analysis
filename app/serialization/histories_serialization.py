from flask_restful import Resource, reqparse, fields, marshal_with
from flask import g

histories_fields = {
    'id': fields.Integer,
    'user_id': fields.Integer,
    'ip ': fields.Integer,
    'url': fields.String,
    'method': fields.String,
    'payload': fields.String,
    'user_agent': fields.String,
    'device_id ': fields.String,
    'device_type': fields.String,
    'app_version': fields.String,
    'os_version': fields.String,
    # 'created_at': fields.datetime,
    # 'updated_at': fields.datetime
}
