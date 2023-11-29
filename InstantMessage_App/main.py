# app.py
from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)
# Mocked user data
users = [
    {"id": 1, "name": "User1"},
    {"id": 2, "name": "User2"},
    # Add more users as needed
]

@app.route('/')
def index():
    #return render_template('index.html', users=users)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
    #socketio.run(app)


# app.py (continued)

socketio = SocketIO(app)


@app.route('/chat/<int:user_id>')
def chat(user_id):
    return render_template('chat.html', user_id=user_id)


@socketio.on('message')
def handle_message(data):
    print('Received message from the client',data)
    #emit('message', data, broadcast=True)
    emit('message_from_server','message received on the server')


if __name__ == '__main__':
    socketio.run(app, debug=True)


"""
Additional considerations
1.User Authentication: Implement user authentication for secure access to the application.
2.Database Integration: Integrate a database to store user information and chat history.
3.Message Persistence: Implement message persistence to store and retrieve chat messages.
4.Security Measures:Implement security measures such as HTTPS, secure sockets, and user authorization.
5.Deployment: Deploy the application to a production server (e.g., Heroku, AWS, or DigitalOcean).
"""

#For user authentication, you can use a library like flask-login
#############
# app.py (continued)
from flask_login import LoginManager, UserMixin, login_required, login_user

login_manager = LoginManager(app)

# Mocked user data
class User(UserMixin):
    def __init__(self, id, name):
        self.id = id
        self.name = name

users = [
    User(1, "User1"),
    User(2, "User2"),
    # Add more users as needed
]

@login_manager.user_loader
def load_user(user_id):
    return next((user for user in users if user.id == int(user_id)), None)

@app.route('/')
@login_required
def index():
    return render_template('index.html', users=users)


#Integratign SQLite for simplicity, install Flask-SQLAlchemy
############
# app.py (continued)
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    sender_id = db.Column(db.Integer, nullable=False)
    receiver_id = db.Column(db.Integer, nullable=False)

db.create_all()

# app.py (continued)
from flask_login import current_user

@app.route('/chat/<int:user_id>')
@login_required
def chat(user_id):
    messages = Message.query.filter(
        (Message.sender_id == current_user.id and Message.receiver_id == user_id) |
        (Message.sender_id == user_id and Message.receiver_id == current_user.id)
    ).all()
    return render_template('chat.html', user_id=user_id, messages=messages)

@socketio.on('message')
def handle_message(data):
    new_message = Message(content=data, sender_id=current_user.id, receiver_id=int(data['user_id']))
    db.session.add(new_message)
    db.session.commit()
    emit('message', data['message'], room=data['user_id'])


# app.py (continued)
from flask_sslify import SSLify
from flask_login import login_required, current_user
from flask_socketio import join_room

# Redirect all HTTP requests to HTTPS
sslify = SSLify(app)

# ...


@socketio.on('connect')
def handle_connect():
    if current_user.is_authenticated:
        join_room(current_user.id)

#In this part we added SSL redirection to ensure all HTTP requests redirect to HTTPS, enhancing security of application
#Additionally we updated the WebSocket connection handling to make sure that users are connected to their respective rooms, improving the isolation of chat rooms.
#####
# app.py (continued)
from flask import url_for

# ...Incorporate the four additional features into the chat application
"""
User Profiles: Allow users to update their profiles, add profile pictures, etc.
File Sharing: Enable users to share files.
Notifications: Implement real-time notifications for new messages.
Search Functionality: Implement a search feature to find messages or users.
"""

@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html')


# app.py (continued)
from flask_uploads import UploadSet, configure_uploads, IMAGES

photos = UploadSet('photos', IMAGES)
app.config['UPLOADED_PHOTOS_DEST'] = 'uploads'
configure_uploads(app, photos)

# ...Include file sharing

@app.route('/chat/<int:user_id>', methods=['GET', 'POST'])
@login_required
def chat(user_id):
    if request.method == 'POST':
        # Handle file upload
        file = request.files['file']
        if file:
            filename = photos.save(file)
            new_message = Message(content=f"File: {filename}", sender_id=current_user.id, receiver_id=user_id)
            db.session.add(new_message)
            db.session.commit()
    messages = Message.query.filter(
        (Message.sender_id == current_user.id and Message.receiver_id == user_id) |
        (Message.sender_id == user_id and Message.receiver_id == current_user.id)
    ).all()
    return render_template('chat.html', user_id=user_id, messages=messages)


# app.py (continued)
from flask_socketio import emit

# ...To implement notifications, you can use Flask-SocketIO to send real-time updates to users

@socketio.on('message')
def handle_message(data):
    new_message = Message(content=data['message'], sender_id=current_user.id, receiver_id=int(data['user_id']))
    db.session.add(new_message)
    db.session.commit()
    emit('message', {'content': data['message'], 'sender_id': current_user.id}, room=data['user_id'])


# app.py (continued)
from sqlalchemy import or_

# ...Creating a search functionality

@app.route('/search', methods=['GET', 'POST'])
@login_required
def search():
    if request.method == 'POST':
        search_query = request.form.get('query')
        users = User.query.filter(or_(User.name.ilike(f'%{search_query}%'))).all()
        return render_template('search_results.html', users=users, query=search_query)
    return render_template('search.html')


"""
[python app.py]
Visit http://127.0.0.1:5000/ in your browser to access the chat application.
Open multiple tabs with different user IDs to simulate multiple users.
"""