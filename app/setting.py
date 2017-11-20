# _*_ coding: utf-8 _*_
import os
from decouple import config

# 调试模式是否开启
DEBUG = config('DEBUG', default=False, cast=bool)

# token过期时间
TIMEOUT = config('TIMEOUT', default=600, cast=int)

basedir = os.path.abspath(__file__)

SQLALCHEMY_TRACK_MODIFICATIONS = False

SQLALCHEMY_POOL_RECYCLE = 5
# session必须要设置key
SECRET_KEY = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

# mysql数据库连接信息,这里改为自己的账号
SQLALCHEMY_DATABASE_URI = config('SQLALCHEMY_DATABASE_URI')
