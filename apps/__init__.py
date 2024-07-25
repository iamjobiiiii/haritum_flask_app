import os
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
login_manager = LoginManager()


def register_extensions(app):
    db.init_app(app)
    login_manager.init_app(app)

from apps.authentication import auth_blueprint
from apps.home import home_blueprint
def register_blueprints(app):
    
    
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(home_blueprint)

def config_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///haritam.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    

def create_app():
    app = Flask(__name__)
    config_db(app)
    register_extensions(app)
    register_blueprints(app)
    
    return app
