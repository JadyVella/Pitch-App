from . import db
from werkzeug.security import generate_password_hash,check_password_hash


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    comment_id = db.Column(db.Integer,db.ForeignKey('comments.id'))

    def __repr__(self):
        return f'User {self.username}'


class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer,primary_key = True)
    pitch_title = db.Column(db.String(255))
    pitch_field = db.Column(db.String)
    users = db.relationship('User',backref = 'comment',lazy = "dynamic")
    pass_secure = db.Column(db.String(255))

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