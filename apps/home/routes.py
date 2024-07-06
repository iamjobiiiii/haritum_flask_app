from flask import render_template
from apps.home import main_bp
from flask_login import login_required


@main_bp.route('/index')
@login_required
def index():
    return render_template('/home/index.html',segment='index')

