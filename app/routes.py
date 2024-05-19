from flask import session, render_template, request, flash, redirect, url_for, jsonify
from app import app, db
from werkzeug.security import generate_password_hash, check_password_hash
from app.model import User, Chat, Message
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
            flash("Successfuly logged in!", "success")
            return redirect(url_for('home'))
        else:
            flash("Invalid username or password",  "warning")
            print("invalid password")
            return redirect(url_for('login'))
    return render_template('loginpage.html')

@app.route('/logout')
def logout():
    print(f"You have been logged out: session = {session}")
    if "user" in session:
        session.pop("user", None)
        flash("You have been logged out!", "success")
        print(" logout successful")
    else:
        flash("Please login first", "warning")
    
    
    return redirect(url_for('login'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        confirmpsw = request.form['confpsw']
        if not len(password) >= 12:
            flash("Password must atleast be 12 characters long", "warning")
            return redirect(url_for('signup'))
        if password != confirmpsw:
            flash("Passwords do not match", "warning")
            return redirect(url_for('signup'))
        
        if User.query.filter_by(username=username).first():
            flash("Username already exists", "warning")
            return redirect(url_for('signup'))
        
        if User.query.filter_by(email=email).first():
            flash("Email already exists", "warning")
            return redirect(url_for('signup'))
        
        passwordhash = generate_password_hash(password)
        newuser = User(username=username, email=email, password=passwordhash)
        db.session.add(newuser)
        db.session.commit()
        flash("Successfully signed up. Thank you!" ,  "success")
        return redirect(url_for('login'))
    return render_template('signup.html')
    
@app.route("/HomePage")
def MainPage():
    return render_template('HomePage.html')



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
    forums = Chat.query.all()  # Get all forums from the database
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
    message_content = request.form['post']

    new_chat = Chat(topic=topic, username=username)
    db.session.add(new_chat)  # Add the new forum to the session
    db.session.commit()  # Commit the session to save the new forum to the database

    # Create a new message associated with the forum
    new_message = Message(content=message_content, chat_id=new_chat.id, user_id=session['user'])
    db.session.add(new_message)
    db.session.commit()

    return redirect(url_for('forum', topic=topic))  # Redirect to the newly created forum

@app.route('/forum/<topic>', methods=['GET', 'POST'])
def forum(topic):
    forum = Chat.query.filter_by(topic=topic).first()
    if forum is None:
        abort(404)
    if request.method == 'POST':
        new_message = Message(content=request.form['content'], chat_id=forum.id, user_id=session['user_id'])
        db.session.add(new_message)
        db.session.commit()
    messages = Message.query.filter_by(chat_id=forum.id).all()
    return render_template('forumtemplate.html', forum=forum, messages=messages)
