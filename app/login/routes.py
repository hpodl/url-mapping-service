import flask
import flask_login as flogin

from . import login
from .login_manager import *
from .forms import LoginForm, RegisterForm


@login.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if flask.request.method == 'POST':
        if form.validate_on_submit():
            nickname = form.username.data
            password = form.password.data
            if register_user(nickname, password):
                return flask.redirect('/')
            else:
                flask.flash("User already exists.")

    return flask.render_template('register.html', form=form)


@login.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if flask.request.method == 'POST':
        if form.validate_on_submit() and load_user(form.username.data):
            user = load_user(form.username.data)

            
            if login_check_credentials(user, form.password.data) and flogin.login_user(user):
                flask.flash('Logged in successfully.')
                return flask.redirect('/')

    
    return flask.render_template('login.html', form=form)


@login.route('/auth_test')
@flogin.login_required
def auth_test():
    return "You are authenticated."