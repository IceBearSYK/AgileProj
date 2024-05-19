import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app, db
from app.model import User, Chat, Message

def populate_db():
    # Create users
    user1 = User(username='john_doe', email='john@example.com', password='hashed_password')
    user2 = User(username='jane_doe', email='jane@example.com', password='hashed_password')    
    # Add users to the session
    db.session.add(user1)
    db.session.add(user2)
    
    # Commit the users to the database
    db.session.commit()
    
    # Create chats
    chat1 = Chat(topic='General Discussion', username=user1.username)
    chat2 = Chat(topic='Project Updates', username=user2.username)
    
    # Add chats to the session
    db.session.add(chat1)
    db.session.add(chat2)
    
    # Commit the chats to the database
    db.session.commit()
    
    # Create messages
    message1 = Message(content='Hello everyone!', user_id=user1.usrID, chat_id=chat1.id)
    message2 = Message(content='Project update: we are on track.', user_id=user2.usrID, chat_id=chat2.id)
    
    # Add messages to the session
    db.session.add(message1)
    db.session.add(message2)
    
    # Commit the messages to the database
    db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        populate_db()
        print("Database populated successfully.")
