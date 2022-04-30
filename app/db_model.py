from flask_sqlalchemy import SQLAlchemy
from hashlib import pbkdf2_hmac as hash
from os import urandom

db = SQLAlchemy()
hash_iterations = 50_000

class User(db.Model):
    id = db.Column(db.INT, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    password_hash = db.Column(db.String(64), nullable=False)
    password_salt = db.Column(db.String(32), nullable=False)

    def __init__(self, name, passwd):
        self.name = name
        self.password_salt = urandom(32)
        self.password_hash = hash('sha256', bytes(passwd, 'utf-8'), self.password_hash, hash_iterations)


class URLMapping(db.Model):
    custom_url = db.Column(db.String(50), primary_key=True)
    target_url = db.Column(db.String(100), nullable=False)

    def __init__(self, custom, target):
            self.custom_url = custom
            self.target_url = target

    def __repr__(self):
        return '<%r -> %r>' % (self.custom_url, self.target_url)