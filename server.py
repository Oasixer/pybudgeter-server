import opencv_test_funcs
from flask import Flask
import sqlite3

conn = sqlite3.connect('database.db')

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)

@app.route('/')
def default():
    return 'test'

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/uploadImg', methods=["POST"])
def uploadImg():
    logger.log(request.files)
    return 'test'
