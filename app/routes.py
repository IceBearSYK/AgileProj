from flask import render_template, request
from app import app
from app.model import user

@app.route('/login')
def login():
    
    
    return render_template('loginpage.html')