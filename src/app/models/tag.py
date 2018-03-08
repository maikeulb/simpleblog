from app.extensions import db
from datetime import datetime, timedelta
from hashlib import md5
from time import time
from flask import current_app
from flask_login import UserMixin
from app.extensions import bcrypt, login
from app.models.post import SearchableMixin
import json
import jwt


class Tag(SearchableMixin, db.Model):
    __tablename__ = 'tags'
    __searchable__ = ['tag']

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
