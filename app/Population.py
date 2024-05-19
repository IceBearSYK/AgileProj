import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app, db
from app.model import User, Chat, Message
from werkzeug.security import generate_password_hash

# Create an application context
with app.app_context():
    # Clear all tables
    db.session.query(User).delete()
    db.session.query(Chat).delete()
    db.session.query(Message).delete()
    db.session.commit()

    # Create new entries
    password='password1'
    user1 = User(username='Bob', email='Bob@example.com', password= generate_password_hash(password))
    user2 = User(username='Steven', email='Steven@example.com', password= generate_password_hash(password))

    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()  # Commit to get the IDs for the users

    chat1 = Chat(topic='topic1', username=user1.usrID)
    chat2 = Chat(topic='topic2', username=user2.usrID)

    db.session.add(chat1)
    db.session.add(chat2)
    db.session.commit()

    message1 = Message(content='content1', chat_id=chat1.id, user_id=user1.usrID)
    message2 = Message(content='content2', chat_id=chat2.id, user_id=user2.usrID)

    # Add new entries to the session
    
    db.session.add(message1)
    db.session.add(message2)

    # Commit the session to write the changes to the database
    db.session.commit()