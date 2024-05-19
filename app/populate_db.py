import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app, db
from app.model import User, Chat, Message
from werkzeug.security import generate_password_hash

def populate_db():
    # Create users
    user1 = User(username='johnyy', email='john@example.com', password= generate_password_hash('1234567891234'))
    user2 = User(username='joeyyy', email='joe@example.com', password=generate_password_hash('1234567891234'))    
    # Add users to the session
    db.session.add(user1)
    db.session.add(user2)
    
    # Commit the users to the database
    db.session.commit()
    
    print("Users in the database:")
    users = User.query.all()
    for user in users:
        print(f"ID: {user.usrID}, Username: {user.username}, Email: {user.email}, Password: {user.password}")
    
    # Create chats
    chat1 = Chat(topic='General Discussion', username=user1.usrID)
    chat2 = Chat(topic='Project Updates', username=user2.usrID)
    
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
