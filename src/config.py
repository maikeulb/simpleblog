import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)


class Config(object):

    WEBPACK_MANIFEST_PATH = '/build/manifest.json'
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(dotenv_path, 'app.db')
    SQLALCHEMY_DATABASE_PASSWORD = os.environ.get('DATABASE_PASSWORD') or \
        'P@ssw0rd!'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    STATIC_FOLDER = 'app/static'

    DEVELOPMENT = False
    TESTING = False
    PRODUCTION = False
    DEBUG = False 
    TESTING = False

class DevelopmentConfig(Config):
    DEBUG = True
    DEVELOPMENT = True
    DEBUG_TB_ENABLED = True
    CACHE_TYPE = 'simple' 

class ProductionConfig(Config):
    DATABASE_URI = ''
    PRODUCTION = True

class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    BCRYPT_LOG_ROUNDS = 4  
    WTF_CSRF_ENABLED = False  
