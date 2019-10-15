import opencv_test_funcs
from flask import Flask
app = Flask(__name__)

@app.route('/')
def default():
    return 'test'

@app.route('/request')
def request():
    return 'Hello, World!'

