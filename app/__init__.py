from flask import Flask

from app.site.routes import site

def create_app(db):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///url.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = app
    db.init_app(app)

    app.register_blueprint(site)
    
    return app
