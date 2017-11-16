# -*- coding:utf-8 -*-
from app import db


class Statistics(db.Model):
    __tablename__ = 'ba_statistics'
    id = db.Column(db.Integer, primary_key=True)
    type_id = db.Column(db.Integer)
    type = db.Column(db.String(255))
    count = db.Column(db.Integer)
    action = db.Column(db.String(255))
    year = db.Column(db.Integer)
    month = db.Column(db.Integer)
    day = db.Column(db.Integer)
    hour = db.Column(db.Integer)
    date = db.Column(db.String(255))
    channel = db.Column(db.String(255))
    ip = db.Column(db.String(255))
    created_at = db.Column(db.String(255))
    updated_at = db.Column(db.String(255))