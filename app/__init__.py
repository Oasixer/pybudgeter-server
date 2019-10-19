from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object('config')

db = SQLAlchemy(app)

from app.mod_auth.controllers import mod_auth as auth_module

app.register_blueprint(auth_module)

db.create_all()

