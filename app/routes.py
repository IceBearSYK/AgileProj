from flask import session, render_template, request, flash, redirect, url_for, jsonify
from app import app, db
from werkzeug.security import generate_password_hash, check_password_hash
from app.model import User, Chat
@app.route("/")
def home():
    return redirect("/HomePage")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print("heyyyy")
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session['user'] = user.usrID
            session['username'] = user.username
            print(f"Session data after login: {session}")
            return redirect(url_for('home'))
        else:
            flash("Invalid username or password")
            print("invalid password")
            return redirect(url_for('login'))
    return render_template('loginpage.html')

@app.route('/logout')
def logout():
    print(f"You have been logged out: session = {session}")
    session.pop("user", None)
    if "user" in session:
        user = session["user"]
        flash("You have been logged out")
    print(" logout successful")
    return redirect(url_for('login'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        confirmpsw = request.form['confpsw']
        
        if password != confirmpsw:
            flash("Passwords do not match")
            return redirect(url_for('signup'))
        
        if User.query.filter_by(username=username).first():
            flash("Username already exists")
            return redirect(url_for('signup'))
        
        if User.query.filter_by(email=email).first():
            flash("Email already exists")
            return redirect(url_for('signup'))
        
        passwordhash = generate_password_hash(password)
        newuser = User(username=username, email=email, password=passwordhash)
        db.session.add(newuser)
        db.session.commit()
        flash("Successfully signed up. Thank you!")
        return redirect(url_for('login'))
    return render_template('signup.html')
    
@app.route("/HomePage")
def MainPage():
    return render_template('HomePage.html')

@app.route("/Forums")
def Forums():
    return render_template('forum.html')

@app.route("/sesh")
def checksesh():
    return f"session right now = {session}"

@app.route("/forgotpassword", methods=['GET', 'POST'])
def forgot():
    return render_template('forgotpassword.html')

@app.route("/reset-password" , methods=['GET', 'POST'] )
def reset():
    return render_template('forgotpasswordresponse.html')

@app.route('/newforum')
def newforum():
    return render_template('newforum.html')
# In-memory storage for chats (for simplicity)


@app.route('/Forums/gaming')
def index():
    session['topic'] = 'Gaming'
    return render_template('Gaming.html')

@app.route('/get_chats', methods=['GET'])
def get_chats():
    topic = session['topic']
    chats = Chat.query.filter_by(topic=topic).all()
    response=[]
    for chat in chats:
        user = User.query.filter_by(usrID=chat.user_id).first()
        response.append({
            'username': user.username,
            'message': chat.message
        })
    return jsonify(response)

@app.route('/send_chat', methods=['POST'])
def send_chat():
    if 'username' not in session:
        return jsonify({"status": "error", "message": "User not logged in"}), 401
    data = request.json
    new_chat = Chat(user_id=session['user'], message=data['message'], topic=session['topic'] )
    print(session['user'])
    print(session['topic'])
    db.session.add(new_chat)
    db.session.commit()
    return jsonify({"status": "success"})
  

