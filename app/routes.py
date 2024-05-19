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

# In-memory storage for chats (for simplicity)
chats = []

@app.route('/Forums')
def forums():
    forums = Chat.query.all()
    return render_template('forum.html', forums=forums)

@app.route('/get_chats', methods=['GET'])
def get_chats():
    return jsonify(chats)

@app.route('/send_chat', methods=['POST'])
def send_chat():
    data = request.json
    chats.append(data)
    return jsonify({"status": "success"})

@app.route('/newforum')
def newforum():
    return render_template('newforum.html')

@app.route('/submit_new_forum', methods=['POST'])
def submit_new_forum():
    if 'user' not in session:
        return redirect(url_for('login'))

    topic = request.form['title']
    username = session['user']  # Assuming the username is stored in session
    message = request.form['post']

    new_chat = Chat(topic=topic, username=username, message=message)
    db.session.add(new_chat)
    db.session.commit()

    flash('Message successfully posted.')
    return redirect(url_for('forum', topic=topic))  # Redirect to the newly created forum

@app.route('/Forums/<topic>')
def forum(topic):
    forum = Chat.query.filter_by(topic=topic).first_or_404()
    return render_template('forumtemplate.html', forum=forum)