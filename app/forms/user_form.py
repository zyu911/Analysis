from flask_restful import Resource, reqparse

user_form = reqparse.RequestParser()
user_form.add_argument('name')
user_form.add_argument('pwd')