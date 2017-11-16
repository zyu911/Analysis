# _*_ coding:utf-8 _*_
from flask_restful import Resource, reqparse

statistics_form = reqparse.RequestParser()
statistics_form.add_argument(
    'type',
    type=str,
    required=True,
    help='type参数是必须的',
)