# _*_ coding: utf-8 _*_
from app import db


class Histories(db.Model):
    __tablename__ = 'ba_action_histories'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(100))
    ip = db.Column(db.String(100))
    url = db.Column(db.String(255))
    method = db.Column(db.String(255))
    payload = db.Column(db.String(2000))
    user_agent = db.Column(db.String(255))
    device_id = db.Column(db.String(255))
    device_type = db.Column(db.String(255))
    app_version = db.Column(db.String(255))
    os_version = db.Column(db.String(255))

    def __init__(self):
        pass

    def __repr__(self):
        return '<histories %r>' % self.id
