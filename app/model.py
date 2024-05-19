from app import db
from werkzeug.security import generate_password_hash

class User(db.Model):
    usrID = db.Column(db.Integer, primary_key = True, autoincrement=True)
    username = db.Column(db.String(12), nullable = False)
    email = db.Column(db.String(20), nullable = False)
    password = db.Column(db.String(200), nullable = False)

class Chat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    topic = db.Column(db.String(30), nullable=False)
    username = db.Column(db.String(80), nullable=False)
    
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.usrID'))  # Changed 'user.id' to 'user.usrID'
    chat_id = db.Column(db.Integer, db.ForeignKey('chat.id'))
