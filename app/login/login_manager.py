from app.db import User, db, hash_iterations
from flask_login import LoginManager
from hashlib import pbkdf2_hmac as hash

login_manager = LoginManager()

@login_manager.user_loader
def load_user(username):
    query_result = User.query.filter_by(name=username).first()
    if query_result:
        return query_result
    
    return None
    

def login_check_credentials(user, password):
    correct_hash = user.password_hash
    salt = user.password_salt
    cur_hash = hash('sha256', bytes(password, 'utf-8'), salt, hash_iterations)

    if cur_hash == correct_hash:
        return True

    return False

def register_user(nickname, password):
    if not User.query.filter_by(name=nickname).first():
        db.session.add(User(nickname, password))
        db.session.commit()
        return True
    else:
        return False
