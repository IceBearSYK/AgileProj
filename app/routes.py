from flask import session, render_template, request, flash, redirect, url_for
from app import app, db
from werkzeug.security import generate_password_hash, check_password_hash
from app.model import User

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        if User.query.filter_by(username==username).first() and check_password_hash(User.password, password): #//checks to see if the username and password matches the username and encrypted password in the database
            session['user'] = User.usrID #if username/password match;  creates a seesion using users id
    return render_template('loginpage.html')
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        confirmpsw = request.form['confpsw']
        if password != confirmpsw:
            flash("passwords do not match")
            return redirect(url_for('signup'))
        if User.query.filter((User.username==username)).first():# checks to see if username is already in the database.
            flash("username already exists")
            return redirect(url_for('signup'))
        if User.query.filter((User.email == email)).first():
            flash("email already exists")
            return redirect(url_for('signup'))
        
        passwordhash = generate_password_hash(password) #encrypts the password before storing it as the password
        newuser = User(username=username, email=email, password = passwordhash)
        db.session.add(newuser)
        db.session.commit()
        flash("Successfully signed up. Thank you!")
        return redirect(url_for('login'))
    else:
         return render_template('signup.html')
    