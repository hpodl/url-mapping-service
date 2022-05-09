from flask import Blueprint
from .login_manager import login_manager

login= Blueprint('login', __name__, template_folder='../templates/login')

