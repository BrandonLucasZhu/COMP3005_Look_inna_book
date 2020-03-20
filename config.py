from flask import Flask
from flask_sqlalchemy import SQLAlchemy

class Config(object):
    DEBUG = True
    DEVELOPMENT = True
    SECRET_KEY = 'do-i-really-need-this'
    FLASK_HTPASSWD_PATH = '/secret/.htpasswd'
    FLASK_SECRET = SECRET_KEY
    DB_HOST = 'database' # a docker link

class Productionconfig(Config):
    DEVELOPMENT = False
    DEBUG = False
    DB_HOST = 'my.production.database' # not a docker link