from app import db


class Request(db.Model):
    __tablename__ = 'requests'
    id = db.Column(db.Integer, primary_key=True)
    method = db.Column(db.String(10), unique=True)
    url = db.Column(db.String(16))
    image_url = db.Column(db.String(16))
    price = db.Column(db.Float)
    uuid = db.Column(db.String(256))

    def __init__(self):
        pass

    def __repr__(self):
        return '<request %r>' % self.id