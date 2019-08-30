from flask import current_app, Blueprint, render_template

adminBP = Blueprint('admin', __name__, url_prefix='/admin', template_folder='templates/', static_folder='static/')

@adminBP.route('/')
def index():
    return render_template('adm-index.html'), 200

@adminBP.route('/users')
def users():
    return render_template('adm-users.html'), 200