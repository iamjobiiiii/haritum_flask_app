from flask import render_template
from home import main_bp

@main_bp.route('/index')
def index():
    return render_template('home/index.html')

@main_bp.route('/')
def dashboard():
    return render_template()