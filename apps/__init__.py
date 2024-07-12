import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def register_blueprint(app):
    blueprint_names = ['auth_bp', 'home_bp']

    for blueprint_name in blueprint_names:
        try:
            module = __import__(f'apps.{blueprint_name}.routes', fromlist=[blueprint_name])  # Import the routes module
            blueprint = getattr(module, f'{blueprint_name}_bp')  # Get the blueprint object from the module
            app.register_blueprint(blueprint)  # Register the blueprint with the Flask app
        except ModuleNotFoundError:
            continue  # Skip if module or blueprint not found

def configure_database(app):
    # app = Flask(_name_)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///haritam.db'  # SQLite database file path
    app.config['SECRET_KEY'] = 'jobin@1231231'  # Secret key for CSRF protection
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Set to False to disable modification tracking

    db.init_app(app)

def create_app():
    app = Flask(__name__)
    configure_database(app)
    register_blueprint(app)
   
    return app