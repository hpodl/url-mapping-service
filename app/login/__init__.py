from flask import Blueprint

from flask_login import LoginManager
from ..db import User
from .login_manager import *

login_manager = LoginManager()
login = Blueprint('login', __name__, template_folder=None)


@login_manager.user_loader
def load_user(username):
    query_result = User.query.filter_by(name=username)
    if query_result:
        return query_result.first()
    
    return None
    