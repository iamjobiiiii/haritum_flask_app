from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy




db = SQLAlchemy()
login_manager = LoginManager()

from apps.authentication.routes import auth_blueprint
from apps.home.routes import auth_blueprint


def register_extensions(app):
    db.init_app(app)
    login_manager.init_app(app)

   

def configure_database(app):
    # app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///haritam.db'  # SQLite database file path
    app.config['SECRET_KEY'] = 'jobin@1231231'  # Secret key for CSRF protection
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.create_all()

def create_app():
    app = Flask(__name__)
    configure_database(app)
    register_extensions(app)
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(auth_blueprint)
    return app