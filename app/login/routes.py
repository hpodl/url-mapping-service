from . import login, load_user, login_check_credentials
from wtforms import LoginForm
import flask

@login.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = load_user(flask.request.args.get('nickname'))
        login_check_credentials(user, flask.request.args.get('password'))

        flask.flash('Logged in successfully.')

        return flask.redirect(next or flask.url_for('index'))
    return flask.render_template('login.html', form=form)