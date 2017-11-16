# -*-coding:utf-8-*-
from flask_restful import fields

statistics_field = {
    "status": fields.String,
    "message": fields.String,
    "data": {
        "data": [
            {"name": "安卓", "data": [1, 1]},
            {"name": "IOS", "data": [0, 0]}
        ],
        "days": ["2017-10-31", None]
    }
}
