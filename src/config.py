from os.path import join, dirname
from dotenv import load_dotenv 

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_DATABASE_PASSWORD= os.environ.get('DATABASE_PASSWORD') or
    'P@ssw0rd!'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

Class ProductionConfig(Config):
    DATABASE_URI = ''

Class DevelopmentConfig(Config):
    DEBUG = True

Class TestingConfig(Config):
    TESTING = True

