from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object('config')

db = SQLAlchemy(app)

#from app.mod_auth.controllers import mod_auth as auth_module
from app.controllers import things

app.register_blueprint(things, url_prefix='/things')

#db.create_all()
