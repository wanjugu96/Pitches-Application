from . import db,create_app
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model,UserMixin):
    __tablename__='users'
    id=db.Column(db.Integer,primary_key =True)
    username=db.Column(db.String(255))
    email=db.Column(db.String(255))
    pass_secure=db.Column(db.String(255))
    bio=db.Column(db.String(255))
    profilepicpath=db.Column(db.String(255))
    comments=db.relationship('Comment',backref='user',lazy='dynamic')
    pitches=db.relationship('Pitch',backref='user',lazy=True)

    @property
    def password(self):
        raise AttributeError('you cannot read the password Attribute')

    @password.setter
    def password(self,password):
        self.pass_secure=generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)        



def __repr__(self):
        return f'User {self.username}'  


class Comment(db.Model):
    __tablename__='comments'
    id=db.Column(db.Integer,primary_key=True)
    comment=db.Column(db.String(255))
    user_id=db.Column(db.Integer,db.ForeignKey('users.id'))
    pitch_id=db.Column(db.Integer,db.ForeignKey('pitches.id'))

    def __repr__(self):
        return f'User {self.comment}'  


class Pitch(db.Model):
    __tablename__='pitches'
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(255))
    category=db.Column(db.String(255))
    pitch=db.Column(db.Text(1000000))
    user_id=db.Column(db.Integer,db.ForeignKey('users.id'))
    name=db.Column(db.String(255))
    comment=db.relationship('Comment',backref='pitches',lazy='dynamic')

   
