
from flask import  render_template
from apps.authentication import auth_bp


@auth_bp.route('/login')
def login():
    return render_template('/accounts/login.html')

@auth_bp.route('/register')
def register():
    return render_template('/accounts/register.html')

