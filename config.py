import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    USER = os.getenv('USER')
    PW = os.getenv('PASSWORD')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        f'postgresql+psycopg2://{USER}:{PW}@/localhost/pybudgeter.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

