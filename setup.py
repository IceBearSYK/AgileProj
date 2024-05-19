from app import app, db

# Ensure we are running within the application context
with app.app_context():
    
    db.drop_all()

    db.create_all()

print("Database tables created successfully.")
