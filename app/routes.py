from flask import session, render_template, request, flash, redirect, url_for, jsonify
from app import app, db
from werkzeug.security import generate_password_hash, check_password_hash
from app.model import User
@app.route("/")
def home():
    return redirect("/HomePage")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session['user'] = user.usrID
            return render_template('HomePage.html')
        else:
            flash("Invalid username or password")
            return render_template('loginpage.html')
    return render_template('loginpage.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        confirmpsw = request.form['confpsw']
        
        if password != confirmpsw:
            flash("Passwords do not match")
            return render_template('signup.html')
        
        if User.query.filter_by(username=username).first():
            flash("Username already exists")
            return render_template('signup.html')
        
        if User.query.filter_by(email=email).first():
            flash("Email already exists")
            return render_template('signup.html')
        
        passwordhash = generate_password_hash(password)
        newuser = User(username=username, email=email, password=passwordhash)
        db.session.add(newuser)
        db.session.commit()
        flash("Successfully signed up. Thank you!")
        return render_template('loginpage.html')
    return render_template('signup.html')
    
@app.route("/HomePage")
def MainPage():
    return render_template('HomePage.html')

@app.route("/Forums")
def Forums():
    return render_template('forum.html')

@app.route("/forgotpassword")
def forgot():
    return render_template('forgotpassword.html')

@app.route("/reset-password")
def reset():
    return render_template('forgotpasswordresponse.html')

# In-memory storage for chats (for simplicity)
chats = []

@app.route('/gaming')
def index():
    return render_template('Gaming.html')

@app.route('/get_chats', methods=['GET'])
def get_chats():
    return jsonify(chats)

@app.route('/send_chat', methods=['POST'])
def send_chat():
    data = request.json
    chats.append(data)
    return jsonify({"status": "success"})