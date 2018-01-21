import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(dotenv_path)


class Config(object):

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'S3cr3t'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or \
      'postgresql://postgres:P@ssw0rd!@172.17.0.2/simpleblog'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # ADMINS = ['michael.sergio.barnes@gmail.com']
    # UPLOAD_FOLDER = os.path.join(INSTANCE_FOLDER_PATH, 'uploads')
    # LOG_FOLDER = os.path.join(INSTANCE_FOLDER_PATH, 'logs')
    # MAX_CONTENT_LENGTH = 16 * 1024 * 1024
    # PROJECT_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['michael.sergio.barnes@gmail.com']
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
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    BCRYPT_LOG_ROUNDS = 4  
    CSRF_ENABLED = False
    WTF_CSRF_ENABLED = False  
