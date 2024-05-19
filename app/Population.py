from app import db, User, Chat, Message

# Clear all tables
db.session.query(User).delete()
db.session.query(Chat).delete()
db.session.query(Message).delete()
db.session.commit()

# Create new entries
user1 = User(username='user1', email='user1@example.com', password='password1')
user2 = User(username='user2', email='user2@example.com', password='password2')

db.session.add(user1)
db.session.add(user2)
db.session.commit()  # Commit to get the IDs for the users

chat1 = Chat(topic='topic1', username=user1.id)
chat2 = Chat(topic='topic2', username=user2.id)

message1 = Message(content='content1', chat_id=chat1.id, user_id=user1.id)
message2 = Message(content='content2', chat_id=chat2.id, user_id=user2.id)

# Add new entries to the session
db.session.add(chat1)
db.session.add(chat2)
db.session.add(message1)
db.session.add(message2)

# Commit the session to write the changes to the database
db.session.commit()