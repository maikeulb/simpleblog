from datetime import datetime
from hashlib import md5
from time import time
from flask import current_app
from flask_login import UserMixin
from app.database import Column, Model, SurrogatePK, db, reference_col, \
    relationship 
from app.extensions import bcrypt, login


class User(UserMixin, Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    email = db.Column(db.String(120), index=True, unique=True, nullable=False)
    password = Column(db.Binary(128), nullable=True)
    first_name = Column(db.String(30), nullable=True)
    last_name = Column(db.String(30), nullable=True)
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime)

    def __init__(self, username, email, password=None, **kwargs):
        db.Model.__init__(self, username=username, email=email, **kwargs)
        if password:
            self.set_password(password)
        else:
            self.password = None

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password)

    # def _get_password(self): // make password into property
    #     return self._password

    def check_password(self, value):
        return bcrypt.check_password_hash(self.password, value)

    @property
    def full_name(self):
        """Full user name."""
        return '{0} {1}'.format(self.first_name, self.last_name)

    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
            digest, size)

    # @classmethod
    # def authenticate(cls, login, password):
    #     user = cls.query.filter(db.or_(
    #         User.name == login, User.email == login)).first()
    #     if user:
    #         authenticated = user.check_password(password)
    #     else:
    #         authenticated = False
    #     return user, authenticated

    # @classmethod
    # def get_by_id(cls, user_id):
    #     return cls.query.filter_by(id=user_id).first_or_404()



@login.user_loader
def load_user(id):
    return User.query.get(int(id))
