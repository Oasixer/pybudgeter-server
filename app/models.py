from datetime import datetime
from hashlib import md5
from time import time
from flask import current_app
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
from app import db#, login

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    balance = db.Column(db.Float, nullable=False)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(320), unique=True, nullable=False)
    transactions = db.relationship("Transactions", backref='user')

    # def __repr__(self):
        # return '<User %r>' % self.username

    def __init__(self, balance, firstname, lastname, email):
        self.balance = balance
        self.firstname = firstname
        self.lastname = lastname
        self.email = email


class Transaction(db.Model):
    __tablename__ = 'transactions'
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer, foreign_key=db.ForeignKey('users.uid'), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)
    delta = db.Column(db.Float, nullable=False) # delta money can be positive or negative
    vendor = db.Column(db.String(800), nullable=False)
    name = db.Column(db.String(800), nullable=False)
    category = db.Column(db.String(800))
    recurring = db.Relationship('Recurring',backref='init')

    def __init__(self, uid, timestamp, delta, vendor, name, category):
        self.uid=uid
        self.timestamp=timestamp
        self.delta=delta
        self.vendor=vendor
        self.name=name
        self.category=category

class Recurring(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tid = db.Column(db.Integer, db.ForeignKey('transactions.id'))
    timedelta = db.Column(db.DateTime)
    n_times = db.Column(db.Integer)

    def __init__(self, tid, timedelta, n_times):
        self.tid = tid
        self.timedelta = timedelta
        self.n_times = n_times

class Categories(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer, db.ForeignKey('users.id'))
    name = db.Column(db.String(800), nullable=False)

    def __init__(self, cid, uid, name):
        self.cid = cid
        self.uid = uid
        self.name = name

# Temp examples


#  class User(UserMixin, db.Model):
    #  id = db.Column(db.Integer, primary_key=True)
    #  username = db.Column(db.String(64), index=True, unique=True)
    #  email = db.Column(db.String(120), index=True, unique=True)
    #  password_hash = db.Column(db.String(128))
    #  posts = db.relationship('Post', backref='author', lazy='dynamic')
    #  about_me = db.Column(db.String(140))
    #  last_seen = db.Column(db.DateTime, default=datetime.utcnow)
    #  followed = db.relationship(
        #  'User', secondary=followers,
        #  primaryjoin=(followers.c.follower_id == id),
        #  secondaryjoin=(followers.c.followed_id == id),
        #  backref=db.backref('followers', lazy='dynamic'), lazy='dynamic')

    #  def __repr__(self):
        #  return '<User {}>'.format(self.username)

    #  def set_password(self, password):
        #  self.password_hash = generate_password_hash(password)

    #  def check_password(self, password):
        #  return check_password_hash(self.password_hash, password)

    #  def avatar(self, size):
        #  digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        #  return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
            #  digest, size)

    #  def follow(self, user):
        #  if not self.is_following(user):
            #  self.followed.append(user)

    #  def unfollow(self, user):
        #  if self.is_following(user):
            #  self.followed.remove(user)

    #  def is_following(self, user):
        #  return self.followed.filter(
            #  followers.c.followed_id == user.id).count() > 0

    #  def followed_posts(self):
        #  followed = Post.query.join(
            #  followers, (followers.c.followed_id == Post.user_id)).filter(
                #  followers.c.follower_id == self.id)
        #  own = Post.query.filter_by(user_id=self.id)
        #  return followed.union(own).order_by(Post.timestamp.desc())

    #  def get_reset_password_token(self, expires_in=600):
        #  return jwt.encode(
            #  {'reset_password': self.id, 'exp': time() + expires_in},
            #  current_app.config['SECRET_KEY'],
            #  algorithm='HS256').decode('utf-8')

    #  @staticmethod
    #  def verify_reset_password_token(token):
        #  try:
            #  id = jwt.decode(token, current_app.config['SECRET_KEY'],
                            #  algorithms=['HS256'])['reset_password']
        #  except:
            #  return
        #  return User.query.get(id)


#  @login.user_loader
#  def load_user(id):
    #  return User.query.get(int(id))


#  class Post(db.Model):
    #  id = db.Column(db.Integer, primary_key=True)
    #  body = db.Column(db.String(140))
    #  timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    #  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    #  language = db.Column(db.String(5))

    #  def __repr__(self):
        #  return '<Post {}>'.format(self.body)
