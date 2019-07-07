from . import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(username):
    return User.query.get(int(username))






class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), index=True)
    email = db.Column(db.String(255), unique=True, index=True)
    pass_secure = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pitch = db.relationship('Pitch', backref='user',lazy='dynamic')
    comments = db.relationship('Comment',backref = 'user',lazy='dynamic')


    @property
    def password(self):
            raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
            self.pass_secure = generate_password_hash(password)

    def verify_password(self, password):
            return check_password_hash(self.pass_secure, password)

    def __repr__(self):
        return f'User {self.username}'


class Pitch(UserMixin,db.Model):
    __tablename__ = 'pitches'
    id = db.Column(db.Integer, primary_key=True)
    text=db.Column(db.Text())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    pitch_category = db.Column(db.String(255))
    posted_at = db.Column(db.DateTime,index=True,default=datetime.utcnow())
    comments = db.relationship('Comment',backref='pitch_id',lazy='dynamic')
    likes=db.Column(db.Integer)
    dislikes=db.Column(db.Integer)


    def save_pitch(self):
             db.session.add(self)
             db.session.commit()

    @classmethod
    def get_pitches(self):
              pitches = Pitch.query.all()
              return pitches

    @classmethod
    def get_pitch(cls,id):
             pitch = Pitch.query.filter_by(id=id).first()
             return pitch

    def display_user(self):
            if Pitch.user_id == User.id:
                    return User.username

    @classmethod
    def count_pitch(cls,username):
        user = User.query.filter_by(username=uname).first()
        pitch = Pitch.query.filter_by(user_id=user.id).all()

        pitch_count= 0
        for pitch in pitches:
            pitch_count +=1
        return pitch_count

class Comment(db.Model):
        __tablename__ = 'comments'
        id = db.Column(db.Integer,primary_key = True)
        user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
        pitches_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))
        pitch_comment = db.Column(db.Text)


        def save_comment(self):
                db.session.add(self)
                db.session.commit()

        @classmethod
        def get_comment(cls,pitches_id):
                comments=Comment.query.filter_by(pitch_id=pitches_id).all()
                return comments
