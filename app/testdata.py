from app import db
from app.model import Chat

new_chat = Chat(username='v', message='hello')
db.session.add(new_chat)