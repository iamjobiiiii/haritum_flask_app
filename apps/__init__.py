import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
from apps.authentication.routes import auth_bp
from apps.home.routes import main_bp


def configure_database(app):
    # app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///haritam.db'  # SQLite database file path
    app.config['SECRET_KEY'] = 'jobin@1231231'  # Secret key for CSRF protection
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

def create_app():
    app = Flask(__name__)
    configure_database(app)
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    return app