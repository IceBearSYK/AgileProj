from app import db
from werkzeug.security import generate_password_hash

class User(db.Model):
    usrID = db.Column(db.Integer, primary_key = True, autoincrement=True)
    username = db.Column(db.String(12), nullable = False)
    email = db.Column(db.String(20), nullable = False)
    password = db.Column(db.String(200), nullable = False)
    