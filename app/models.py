from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    pitches = db.relationship('Pitch',backref = 'user',lazy = "dynamic")
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String(80))
    password_secure = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_secure = generate_password_hash(password)
        return self.password_secure


    def verify_password(self,password):
        return check_password_hash(self.password_secure,password)

    def __repr__(self):
        return f'User {self.username}'
        
class Pitch(db.Model):
    __tablename__ = 'pitches'
    id = db.Column(db.Integer,primary_key = True)
    category = db.Column(db.String(70))
    pitch = db.Column(db.Text)
    date_posted = db.Column(db.DateTime,default=datetime.utcnow)
    upvotes = db.Column(db.Integer, default=0)
    downvotes = db.Column(db.Integer, default=0)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))

    def __repr__(self):
        return f'Pitch {self.pitch}'

        
class Comments(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer,primary_key = True)
    comment = db.Column(db.Text)
    date_posted = db.Column(db.DateTime,default=datetime.utcnow)

    def __repr__(self):
        return f'Comment {self.pitch}'

class Feedback(db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(100))
    feedback = db.Column(db.Text)
    date_posted = db.Column(db.DateTime,default=datetime.utcnow)

    def __repr__(self):
        return f'Feedback {self.pitch}'
# class Upvote(db.Model):
#     __tablename__ = 'upvotes'

#     id = db.Column(db.Integer,primary_key = True)
#     pitch_id = db.Column(db.Integer)
#     votes = db.Column(db.String(70))
#     user_id = db.Column(db.Integer,db.ForeignKey("users.id"))

#     def __repr__(self):
#         return f'Upvote {self.votes}'


# class Downvote(db.Model):
#     __tablename__ = 'downvotes'

#     id = db.Column(db.Integer,primary_key = True)
#     pitch_id = db.Column(db.Integer)
#     votes = db.Column(db.String(70))
#     user_id = db.Column(db.Integer,db.ForeignKey("users.id"))


#     def __repr__(self):
#         return f'User {self.votes}'



class Rolek(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))


    def __repr__(self):
        return f'User {self.name}'


# class Review(db.Model):

#     __tablename__ = 'reviews'

#     id = db.Column(db.Integer,primary_key = True)
#     movie_id = db.Column(db.Integer)
#     movie_title = db.Column(db.String)
#     image_path = db.Column(db.String)
#     movie_review = db.Column(db.String)
#     posted = db.Column(db.DateTime,default=datetime.utcnow)
#     user_id = db.Column(db.Integer,db.ForeignKey("users.id"))

#     def save_review(self):
#         db.session.add(self)
#         db.session.commit()

#     @classmethod
#     def get_reviews(cls,id):
#         reviews = Review.query.filter_by(movie_id=id).all()
#         return reviews


