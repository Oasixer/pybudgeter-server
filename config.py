import os
from dotenv import load_dotenv
load_dotenv()

USER = os.getenv('USER')
PW = os.getenv('PASSWORD')

DEBUG = True

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = f'postgresql://{USER}:{PW}@localhost/pybudgeter.db')

THREADS_PER_PAGE = 2

