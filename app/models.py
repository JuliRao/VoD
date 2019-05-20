from _datetime import datetime
from app import db

# admin
class AdminUser(db.Model):
    __tablename__ = "admin_user"
    name = db.Column(db.String(100), unique=True, primary_key=True)
    pwd = db.Column(db.String(100))
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return "<User %r>" % self.name

    def check_pwd(self, pwd):
        return self.pwd == pwd


class Movie(db.Model):
    __tablename__ = 'movie'
    #id = db.Column(db.Integer)
    title = db.Column(db.String(255), unique=True, primary_key=True)
    url = db.Column(db.String(255), unique=True)
    info = db.Column(db.Text)
    logo = db.Column(db.String(255), unique=True)
    speaker = db.Column(db.String(255))
    speaker_info = db.Column(db.Text)

    def __repr__(self):
        return '<Movie %r>' % self.title
