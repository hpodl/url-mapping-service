import flask

from . import site
from ..db import db, URLMapping, User

@site.route('/', methods=['GET', 'POST'])
def main_page():
        custom = None
        target = None

        if flask.request.method == 'POST':
            custom = (flask.request.form.get('custom_url'))
            target = (flask.request.form.get('target_url'))

            if not URLMapping.query.filter_by(custom_url=custom).first():
                db.session.add(URLMapping(custom, target))
                db.session.commit()
            else:
                flask.flash("Custom url is already taken.")

        return flask.render_template('site/main_page.html')

@site.route('/s/<custom_code>')
def custom_redirect(custom_code):
    target = URLMapping.query.filter_by(custom_url=custom_code).first()
    if not target:
        flask.flash("Nonexistent custom url.")
        return flask.redirect('/')

    target = target.target_url
    if target.find("http://") != 0 and target.find("https://") != 0:
        target = "http://" + target

    return flask.redirect(target)



@site.route('/register', methods=['GET', 'POST'])
def register():
        if flask.request.method == 'POST':
            nickname = (flask.request.form.get('nickname'))
            password = (flask.request.form.get('password'))

            if not User.query.filter_by(name=nickname).first():
                db.session.add(User(nickname,password))
                db.session.commit()
            else:
                flask.flash("User already exists.")

        return flask.render_template('site/register_page.html')
