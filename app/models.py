from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
import datetime


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    '''
     User class to define user Objects
    '''
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20),unique=True, nullable=False)
    email = db.Column(db.String(120),unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    date_joined = db.Column(db.DateTime,default=datetime.datetime.utcnow)
    password = db.Column(db.String(60), nullable=False)
    notes = db.relationship('Notes', backref='author', lazy=True)
    def __repr__(self):
        return f"User('{self.username}', '{self.email}','{self.image_file}')"








