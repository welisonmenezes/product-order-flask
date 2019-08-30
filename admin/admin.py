from flask import Blueprint, render_template

adminBP = Blueprint('admin', __name__, url_prefix='/admin', template_folder='templates/')

@adminBP.route('/')
def index():
    return render_template('dashboard.html'), 200

@adminBP.route('/users')
def users():
    return render_template('users.html'), 200