from apps.home import main_bp
from flask_login import login_required
from flask import render_template, request
from flask_login import login_required
from jinja2 import TemplateNotFound


@main_bp.route('/index')
@login_required
def index():

    return render_template('home/index.html', segment='index')


@main_bp.route('/<template>')
@login_required
def route_template(template):

    try:

        if not template.endswith('.html'):
            template += '.html'

        # Detect the current page
        segment = get_segment(request)

        # Serve the file (if exists) from app/templates/home/FILE.html
        return render_template("home/" + template, segment=segment)

    except TemplateNotFound:
        return  404

    except:
        return  500


# Helper - Extract current page name from request
def get_segment(request):

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment

    except:
        return None