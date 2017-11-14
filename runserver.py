from app import manager
from flask.ext.httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()


if __name__ == '__main__':
    manager.run()
