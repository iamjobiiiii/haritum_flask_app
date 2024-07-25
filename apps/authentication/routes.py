
from flask import  render_template, redirect, url_for,request
from flask_login import login_user, logout_user,login_required
from forms import LoginForm, RegistrationForm
from models import User, db
from .import auth_blueprint


from flask_login import (
    current_user,
    login_user,
    logout_user
)

@auth_blueprint.route('/')
def route_default():
    return redirect(url_for('home_bp.index'))


# Login & Registration

@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm(request.form)
    if 'login' in request.form:
       

        # read form data
        username = request.form['username']
        password = request.form['password']

        # Locate user
        user = User.query.filter_by(username=username).first()

        # Check the password
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('auth_bp.route_default'))


        # Something (user or pass) is not ok
        return render_template('accounts\login.html',
                               msg='Wrong user or password',
                               form=login_form)

    if not current_user.is_authenticated:
        return render_template('accounts\login.html',
                               form=login_form)
    return redirect(url_for('auth_bp.index'))


@auth_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    create_account_form = RegistrationForm(request.form)
    if 'register' in request.form:

        username = request.form['username']
        email = request.form['email']

        # Check usename exists
        user = User.query.filter_by(username=username).first()
        if user:
            return render_template('accounts/register.html',
                                   msg='Username already registered',
                                   success=False,
                                   form=create_account_form)

        # Check email exists
        user = User.query.filter_by(email=email).first()
        if user:
            return render_template('accounts/register.html',
                                   msg='Email already registered',
                                   success=False,
                                   form=create_account_form)

        # else we can create the user
        user = User(**request.form)
        db.session.add(user)
        db.session.commit()

        return render_template('accounts/register.html',
                               msg='User created please <a href="/login">login</a>',
                               success=True,
                               form=create_account_form)

    else:
        return render_template('accounts/register.html', form=create_account_form)


@auth_blueprint.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth_bp.login'))



#   admin register     

# @auth_blueprint.route('/admin', methods=['POST'])
# def admin():
#     if not request.json or not 'username' in request.json or not 'password' in request.json:
#         return jsonify({'message': "No username or password found!"}), 400
#     else:
#         username =  request.json['username']
#         password =  request.json['password']
#         existing_user = Admin.query.filter_by(username=username).first()
#         if existing_user:
#             return jsonify({'message': "Username is already found!"}), 403
#         new_admin = Admin(username=username, password=password)
#         db.session.add(new_admin)
#         db.session.commit()
#         return jsonify(new_admin.__str__), 201

# #  agent register
# @auth_blueprint.route('/agent', methods=['GET','POST']) 
# def agent_reg():
#     if 'agent' in request.form:
#         username = request.form['username']
#         password = request.form['password']
#         email = request.form['email']
#         phone_number = request.form['phone_number']


#         existing_agent = Agent.query.filter_by(username=username).first()     
       
        
#         if existing_agent:
#           return render_template('/home/register.html',msg='Username already registered',success=False,
#                                    form=request.form)
#         new_agent = Agent(username=username, email=email, phone_number=phone_number, password=password)
#         db.session.add(new_agent)
#         db.session.commit()

#         return render_template('/home/register.html',
#                                msg='New agent created ',
#                                success=True,
#                                form=request.form)
#     else:
#             return render_template('/home/register.html', form=request.form)

        

