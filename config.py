import os

from sqlalchemy import create_engine

import urllib

class Config(object):
    SECRET_KEY = 'HOLA'
    SESSION_COOKIE_SECURE = False

class DevelpmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@127.0.0.1/idgs801'
    SQLALCHEMY_TRACK_MODIFICATION = False