from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app import db


class User(db.Model):
    __tablename__ = 'users'
    uid = db.Column(db.Integer, primary_key=True)
    balance = db.Column(db.Float, nullable=False)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(320), unique=True, nullable=False)
    transactions = db.relationship("Transactions")

    # def __repr__(self):
        # return '<User %r>' % self.username

    def __init__(self, uid, balance, firstname, lastname, email):
        self.uid = uid
        self.balance = balance
        self.firstname = firstname
        self.lastname = lastname
        self.email = email


class Transaction(db.Model):
    __tablename__ = 'transactions'
    tid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    uid = db.Column(db.Integer, foreign_key=db.ForeignKey('users.uid'), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)
    delta = db.Column(db.Float, nullable=False) # delta money can be positive or negative
    vendor = db.Column(db.String(800), nullable=False)
    name = db.Column(db.String(800), nullable=False)
    category = db.Column(db.String(800))
    recurring = db.Relationship('recurring')

    def __init__(self, id, uid, timestamp, delta, vendor, name, category):
        self.id=id
        self.uid=uid
        self.timestamp=timestamp
        self.delta=delta
        self.vendor=vendor
        self.name=name
        self.category=category

class Recurring(db.Model):
    rid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fid = db.Column(db.I)
    timedelta = db.Column(db.DateTime)
    n_times = db.Column(db.Integer)



