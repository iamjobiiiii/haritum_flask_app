from flask import render_template, redirect, request, url_for,jsonify
from apps import db,login_manager
from apps.authentication import auth_blueprint
from apps.authentication.models import User, Admin,Agent

from flask_login import ( login_user, logout_user, current_user)


# Login & Registration
@auth_blueprint.route('/')
def route_default():
    return redirect(url_for('auth_bp.login'))

@auth_blueprint.route('/login' ,methods=['GET','POST'])
def login():
    if request.method == 'POST' and login in request.form:
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('auth_bp.route_default'))

        # Something (user or pass) is not ok
        return render_template('/accounts/login.html', msg='Wrong user or password', form=request.form)

    print(current_user.is_authenticated)
    if not current_user.is_authenticated:
        return render_template('/accounts/login.html',  form=request.form)
    return redirect(url_for('home_bp.index'))

#  user register       

@auth_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    if 'register' in request.form:
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        phone_number = request.form['phone_number']
       
        existing_user = User.query.filter_by(username=username).first()

        if existing_user:
            return render_template('/accounts/register.html',
                                   msg='Username already registered',
                                   success=False,
                                   form=request.form)

        new_user = User(username=username, email=email, phone_number=phone_number, password=password)
        db.session.add(new_user)
        db.session.commit()

        return render_template('/accounts/register.html',
                               msg='User created please <a href="/login">login</a>',
                               success=True,
                               form=request.form)
    else:
            return render_template('/accounts/register.html', form=request.form)



#   admin register     

@auth_blueprint.route('/admin', methods=['POST'])
def admin():
    if not request.json or not 'username' in request.json or not 'password' in request.json:
        return jsonify({'message': "No username or password found!"}), 400
    else:
        username =  request.json['username']
        password =  request.json['password']
        existing_user = Admin.query.filter_by(username=username).first()
        if existing_user:
            return jsonify({'message': "Username is already found!"}), 403
        new_admin = Admin(username=username, password=password)
        db.session.add(new_admin)
        db.session.commit()
        return jsonify(new_admin.__str__), 201

#  agent register
@auth_blueprint.route('/agent', methods=['GET','POST']) 
def agent_reg():
    if 'agent' in request.form:
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        phone_number = request.form['phone_number']


        existing_agent = Agent.query.filter_by(username=username).first()     
       
        
        if existing_agent:
          return render_template('/home/register.html',msg='Username already registered',success=False,
                                   form=request.form)
        new_agent = Agent(username=username, email=email, phone_number=phone_number, password=password)
        db.session.add(new_agent)
        db.session.commit()

        return render_template('/home/register.html',
                               msg='New agent created ',
                               success=True,
                               form=request.form)
    else:
            return render_template('/home/register.html', form=request.form)

        

