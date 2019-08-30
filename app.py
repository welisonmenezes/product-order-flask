from flask import Flask, render_template
from admin import admin as adm

def create_app():

    # start Flask app
    app = Flask(__name__)
    
    # apply app configurations
    app.config.from_pyfile('config.py')

    # routes all nonexistent route to /
    @app.route('/')
    def index():
        return render_template('index.html'), 200

    @app.route('/produtos')
    def produtos():
        return render_template('products.html'), 200

    # initialize the api blueprint
    app.register_blueprint(adm.adminBP)

    return app