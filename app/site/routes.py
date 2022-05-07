import flask
from flask_login import current_user, login_required

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
                mapping = URLMapping(custom, target)
                db.session.add(mapping)
                if current_user and current_user.is_authenticated:
                    current_user.mappings.append(mapping)
                
                db.session.commit()
            else:
                flask.flash("Custom url is already taken.")

        return flask.render_template('site/index.html')

@site.route('/<custom_code>')
def custom_redirect(custom_code):
    target = URLMapping.query.filter_by(custom_url=custom_code).first()
    if not target:
        flask.flash("Nonexistent custom url.")
        return flask.redirect('/')

    target = target.target_url
    if target.find("http://") != 0 and target.find("https://") != 0:
        target = "http://" + target

    return flask.redirect(target)


@site.route('/manage', methods=['GET', 'POST'])
@login_required
def manage():
    if flask.request.method == 'POST':
        if flask.request.form.get('mappingid').isalnum():
            id = flask.request.form.get('mappingid')   
            db.session.delete(URLMapping.query.filter_by(custom_url=id).first())
            db.session.commit()
            
    return flask.render_template('site/manage.html')
