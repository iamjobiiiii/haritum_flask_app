from ..import db,login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone_number = db.Column(db.String(15))
    password = db.Column(db.String(128), nullable=False)
    
    def set_password(self, password):
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password, password)



# class Admin(db.Model,UserMixin):
#     __tablename__ = 'admin'
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(20), unique=True, nullable=False)
#     password = db.Column(db.String(128), nullable=False)


#     def check_admin_pass(self, password): 
#         return self.password == password

# class Agent(db.Model,UserMixin): 
#        __tablename__ = 'agent'
#        id = db.Column(db.Integer, primary_key=True)
#        email = db.Column(db.String(120), unique=True, nullable=False)
#        phone_number = db.Column(db.String(20), unique=True, nullable=False)
#        username = db.Column(db.String(20), unique=True, nullable=False)
#        password = db.Column(db.String(128), nullable=False)


#        def __init__(self, username, email, phone_number, password):
#           self.username = username
#           self.email = email
#           self.phone_number = phone_number
#           self.salt = os.urandom(16).hex() 

       
#           self.password = generate_password_hash(password + self.salt)

#        def check_password(self, password):
       
#           return check_password_hash(self.password, password + self.salt)











@login_manager.user_loader
def load_user(user_id):
        return User.query.get(int(user_id))


# @login_manager.request_loader
# def request_loader(request):
#     username = request.form.get('username')
#     user = User.query.filter_by(username=username).first()
#     return user if user else None