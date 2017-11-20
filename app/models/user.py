# _*_ coding: utf-8 _*_
from app import db
from passlib.apps import custom_app_context as pwd_context
from itsdangerous import SignatureExpired, BadSignature, TimedJSONWebSignatureSerializer as Serializer
from app import setting
import bcrypt


class User(db.Model):
    __tablename__ = 'ba_admin_users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), index=True)
    email = db.Column(db.String(128))
    password = db.Column(db.String(128))
    remember_token = db.Column(db.String(100))
    created_at = db.Column(db.String(100))
    updated_at = db.Column(db.String(100))

    def __init__(self, email, password_hash=None):
        self.name = email
        self.email = email
        self.password = password_hash

    def hash_password(self, password):
        self.password = bcrypt.hashpw(str(password), bcrypt.gensalt())

    def verify_password(self, password):
        hash = str(self.password)
        hash_new = bcrypt.hashpw(password, hash)
        return True if hash == hash_new else False

    def __repr__(self):
        return '<User %r>' % self.name

    def generate_auth_token(self, expiration=setting.TIMEOUT):
        s = Serializer(setting.SECRET_KEY, expires_in=expiration)
        return s.dumps({'id': self.id})

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(setting.SECRET_KEY)
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None  # valid token, but expired
        except BadSignature:
            return None  # invalid token
        user = User.query.get(data['id'])
        return user



