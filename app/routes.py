from flask import render_template
from app import app

@app.route('/login')
def login():
    return render_template('loginpage.html')