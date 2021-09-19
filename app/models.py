from . import db
class User(db.Model):
    __tablename__='users'
    id=db.Column(db.Integer,primary_key =True)
    username=db.Column(db.String(255))
    email=db.Column(db.String(255))
    password=db.Column(db.String(255))
    comments=db.relationship('Comment',backref='users',lazy='dynamic')
    pitch=db.relationship('Pitch',backref='users',lazy='dynamic')


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
    pitch=db.Column(db.String(255))
    user_id=db.Column(db.Integer,db.ForeignKey('users.id'))
    comment=db.relationship('Comment',backref='pitches',lazy='dynamic')


    def __repr__(self):
        return f'User {self.title}'
