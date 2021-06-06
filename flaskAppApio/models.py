from flask_login import UserMixin
from . import db
from datetime import datetime
import time

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(100) )

class time1(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time1_name = db.Column(db.String(200), nullable=False)
    time1_date_created = db.Column(db.DateTime, default=datetime.utcnow)
    time1_type = db.Column(db.String(200), nullable=False)

class kw1(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    kw1_name = db.Column(db.String(100), nullable=False)

