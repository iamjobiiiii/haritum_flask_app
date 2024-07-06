from apps import db
from werkzeug.security import generate_password_hash, check_password_hash
import os

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone_number = db.Column(db.String(20), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    salt = db.Column(db.String(32), nullable=False)  # Store a salt for added security

    def __init__(self, username, email, phone_number, password):
        self.username = username
        self.email = email
        self.phone_number = phone_number
        self.salt = os.urandom(16).hex()  # Generate a random salt

        # Hash the password with the salt
        self.password_hash = generate_password_hash(password + self.salt)

    def check_password(self, password):
        # Check if the provided password matches the stored hashed password
        return check_password_hash(self.password_hash, password + self.salt)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"
