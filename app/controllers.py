import opencv_test_funcs
from flask import Blueprint

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

things = Blueprint('things', __name__)

@things.route('/')
def default():
    return 'test'

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@things.route('/uploadImg', methods=["POST"])
def uploadImg():
    logger.log(request.files)
    return 'test'
