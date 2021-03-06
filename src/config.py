import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(dotenv_path)


class Config(object):

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'S3cr3t'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or \
      'postgresql://postgres:P@ssw0rd!@postgres/simpleblog'
    ELASTICSEARCH_URL=os.environ.get('ELASTIC_URI') or \
      'http://elastic'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')

    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['michael.sergio.barnes@gmail.com']
    ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL')
    POSTS_PER_PAGE = 10

    DEBUG_TB_INTERCEPT_REDIRECTS = False
    DEVELOPMENT = False
    TESTING = False
    PRODUCTION = False
    DEBUG = False
    TESTING = False

class DevelopmentConfig(Config):
    DEBUG = True
    DEVELOPMENT = True
    DEBUG_TB_ENABLED = True
    # CACHE_TYPE = 'simple'

class ProductionConfig(Config):
    DATABASE_URI = ''
    PRODUCTION = True

class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    BCRYPT_LOG_ROUNDS = 4
    CSRF_ENABLED = False
    WTF_CSRF_ENABLED = False
