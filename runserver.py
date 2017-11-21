from flask.ext.httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()
from app import manager
from app import app

if __name__ == '__main__':
    manager.run()
