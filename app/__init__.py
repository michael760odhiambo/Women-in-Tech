from flask_script import Manager,Server
from flask import Flask
from.config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


bootstrap = Bootstrap()
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    #initalizing extensions
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://lilibeth:1234@localhost/tech'
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')

    return app