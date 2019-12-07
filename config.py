import os
from dotenv import load_dotenv
load_dotenv()

USER = os.getenv('USER')
PW = os.getenv('PASSWORD')

DEBUG = True

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://{USER}:{PW}@/localhost/pybudgeter.db'

SQLALCHEMY_TRACK_MODIFICATIONS = False

THREADS_PER_PAGE = 2

