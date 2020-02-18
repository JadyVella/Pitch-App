from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    comment_id = db.Column(db.Integer,db.ForeignKey('comments.id'))
    password_hash = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))


    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.pass_secure,password)



    def __repr__(self):
        return f'User {self.username}'


class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer,primary_key = True)
    pitch_title = db.Column(db.String(255))
    pitch_field = db.Column(db.String)
    users = db.relationship('User',backref = 'comment',lazy = "dynamic")


    def __repr__(self):
        return f'User {self.pitch_field}'


class PICKUPLINES:
    all_pickuplines = []
    def __init__(self,title,pitch):
        self.title = title
        self.pitch = pitch

    def save_pickupline(self):
        PICKUPLINES.all_pickuplines.append(self)


    @classmethod
    def clear_pitchs(cls):
        PICKUPLINES.all_pickuplines.clear()


    @classmethod
    def get_pitchs(cls):

        response = []

        for pitchs in cls.all_pickuplines:
            response.append(pitchs)

        return response
        


class INTERVIEW:
    all_interview = []
    def __init__(self,title,pitch):
        self.title = title
        self.pitch = pitch

    def save_interview(self):
        INTERVIEW.all_interview.append(self)


    @classmethod
    def clear_pitchs(cls):
        PICKUPLINES.all_pickuplines.clear()


    @classmethod
    def get_pitchs(cls):

        response = []

        for pitchs in cls.all_interview:
            response.append(pitchs)

        return response


class BUSINESSPLAN:
    all_businessplan = []
    def __init__(self,title,pitch):
        self.title = title
        self.pitch = pitch

    def save_businessplan(self):
        BUSINESSPLAN.all_businessplan.append(self)