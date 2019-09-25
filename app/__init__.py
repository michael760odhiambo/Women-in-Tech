from flask_script import Manager,Server
from flask import Flask
from.config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap


bootstrap = Bootstrap()
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    #initalizing extensions
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://lilibeth:1234@localhost/tech'
    bootstrap.init_app(app)
    db.init_app(app)
    return app