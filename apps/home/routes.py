from flask import render_template
from apps.home import main_bp



@main_bp.route('/')
def index():
    return render_template('/home/index.html')