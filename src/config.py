import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(dotenv_path)


class Config(object):

    WEBPACK_MANIFEST_PATH = '/build/manifest.json'
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_DATABASE_PASSWORD = os.environ.get('DATABASE_PASSWORD') or \
        'P@ssw0rd!'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # ADMINS = ['michael.sergio.barnes@gmail.com']
    # UPLOAD_FOLDER = os.path.join(INSTANCE_FOLDER_PATH, 'uploads')
    # LOG_FOLDER = os.path.join(INSTANCE_FOLDER_PATH, 'logs')
    # MAX_CONTENT_LENGTH = 16 * 1024 * 1024
    # PROJECT_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

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
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    BCRYPT_LOG_ROUNDS = 4  
    CSRF_ENABLED = False
    WTF_CSRF_ENABLED = False  
