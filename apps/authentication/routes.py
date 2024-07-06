
from flask import render_template, redirect, request, url_for
from apps import db
from apps.authentication import auth_bp
from apps.authentication.models import User

from flask_login import (
    current_user,
    login_user,
    logout_user
)




# Login & Registration
@auth_bp.route('/')
def route_default():
    return redirect(url_for('auth_bp.login'))

@auth_bp.route('/login' ,methods=['POST'])
def login():
       if 'login' in request.form:
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('auth_bp.route_default'))

        # Something (user or pass) is not ok
        return render_template('/accounts/login.html',
                               msg='Wrong user or password',
                               form=request.form)

       if not current_user.is_authenticated:
            return render_template('/accounts/login.html',
                               form=request.form)
       return redirect(url_for('home_bp.index'))
        

@auth_bp.route('/register', methods=['GET', 'POST'])
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


    