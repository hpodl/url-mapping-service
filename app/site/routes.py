import flask

from . import site
from ..db_model import db, URLMapping

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
