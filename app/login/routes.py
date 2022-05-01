import flask
import flask_login as flogin

from . import login
from .login_manager import load_user, login_check_credentials
from .forms import LoginForm

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