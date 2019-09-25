from flask import Flask
from.config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap


bootstrap = Bootstrap()
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    #initalizing extensions
    boostrap.init_app(app)
    db.init_app(app)
    return app