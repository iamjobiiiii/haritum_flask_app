import os
from flask import Flask
from apps.authentication.routes import auth_bp
from apps.home.routes import main_bp
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
def configure_database(app):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///haritam.db'  # SQLite database file path
    app.config['SECRET_KEY'] = 'your_secret_key_here'  # Secret key for CSRF protection
    db.init_app(app)

def create_app():
    app = Flask(__name__)
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    configure_database(app)
    return app