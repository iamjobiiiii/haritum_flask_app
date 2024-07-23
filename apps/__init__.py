from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key_here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///haritam.db'  # SQLite database, change as per your DBMS
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)
    login_manager.init_app(app)
    
    
    from apps.authentication import auth_blueprint
    from apps.home import home_blueprint
    
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(home_blueprint)
    
   
    
    return app
