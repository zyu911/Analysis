from flask_restful import Resource, reqparse

user_form = reqparse.RequestParser()
user_form.add_argument(
    'email',
    type=str,
    required=True,
    help='Email cannot be blank!'
    )
user_form.add_argument(
    'password',
    type=str,
    required=True,
    help='Password cannot be blank!'
)