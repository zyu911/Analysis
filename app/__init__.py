# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from . import setting
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_restful import Api
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
api = Api(app)

app.config.from_object('app.setting')

# os.environ['FLASKR_SETTINGS'] = setting.basedir
# env = os.environ.get('FLASKR_SETTINGS')
# print(env, '----->')
app.config['FLASKR_SETTINGS'] = setting.basedir
db = SQLAlchemy(app)

manager = Manager(app)
migrate = Migrate(app, db)
# print(manager.__dict__)
manager.add_command('db', MigrateCommand)


from app.models.user import *
from app.models.admin import *
from app.controller import account_views
from app.controller import histories_views
from app.controller import statistics_views
from app import routes


