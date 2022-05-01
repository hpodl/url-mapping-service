from flask import Flask

from app.site.routes import site
from app.login.routes import login

def create_app(db, login_manager):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///url.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = app
    db.init_app(app)

    login_manager.init_app(app)

    app.register_blueprint(site)
    app.register_blueprint(login)
    
    return app
