from flask_sqlalchemy import flask_sqlalchemy

boostrap = Boostrap()
db = SQLAlchemy()

def create_app(config_name)
#initalizing extensions
boostrap.init_app(app)
db.init_app(app)