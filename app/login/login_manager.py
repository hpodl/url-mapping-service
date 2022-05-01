import app.db as db

def login_check_credentials(user, password):
    correct_hash = user.password_hash
    salt = user.password_salt

    hash = password_hash = hash('sha256', bytes(password, 'utf-8'), salt, db.hash_iterations)
    if hash == correct_hash:
        return True

    return False

