#import opencv_test_funcs
import base64
from flask import Blueprint, request

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

things = Blueprint('things', __name__)

@things.route('/')
def default():
    return 'test'

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@things.route('/uploadImg', methods=["POST"])
def uploadImg(**kwargs):
   # logger.log(request.files)
    return 'test'

@things.route('/testUpload', methods=['POST'])
def testUpload():
  rawImage = request.get_data()
  rawImage = rawImage['image']

  with open('../testPics/testpic.jpeg', 'wb') as fh:
    fh.write(base64.decodebytes(rawImage))

  return 'Success'
