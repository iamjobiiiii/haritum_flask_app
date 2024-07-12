import os
from werkzeug.security import generate_password_hash, check_password_hash
from apps import db


class User(db.Model):
    _tablename_ = 'Users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone_number = db.Column(db.String(20), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    salt = db.Column(db.String(32), nullable=False)  # Store a salt for added security

    def _init_(self, username, email, phone_number, password):
        self.username = username
        self.email = email
        self.phone_number = phone_number
        self.salt = os.urandom(16).hex()  # Generate a random salt  

        # Hash the password with the salt
        self.password_hash = generate_password_hash(password + self.salt)

    def check_password(self, password):
        # Check if the provided password matches the stored hashed password
        return check_password_hash(self.password_hash, password + self.salt)

    def _repr_(self):
        return f"User('{self.username}', '{self.email}')"
    



class Admin(db.Model):
    _tablename_ = 'admin'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)


    def _init_(self, username,  password):
           self.username = username
           self.salt = os.urandom(16).hex() 
           self.password = generate_password_hash(password + self.salt)

    def check_password(self, password):
        
        return check_password_hash(self.password, password + self.salt)

    def _repr_(self):
        return f"User('{self.username}', '{self.password}')"
    

class Agent(db.Model): 
       _tablename_ = 'agent'

       agent_id = db.Column(db.Integer, primary_key=True)
       agent_username = db.Column(db.String(20), unique=True, nullable=False)
       password_hash = db.Column(db.String(128), nullable=False)

def check_agent_pass(self,password): 
    return False