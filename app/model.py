from app import db
from werkzeug.security import generate_password_hash

class User(db.Model):
    usrID = db.Column(db.Integer, primary_key = True, autoincrement=True)
    username = db.Column(db.String(12), nullable = False)
    email = db.Column(db.String(20), nullable = False)
    password = db.Column(db.String(200), nullable = False)
    chats = db.relationship('Chat', backref='user', lazy=True)


class Chat(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.usrID'), nullable=False)
    message = db.Column(db.String(200), nullable=False)
    topic = db.Column(db.String(30), nullable=False)
