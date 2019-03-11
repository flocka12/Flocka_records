''' module for creating app '''
from flask import Flask
from .api.v1 import VERSION_ONE

def create_app():
    ''' creates app and registers blueprints '''
    app = Flask(__name__)
    app.register_blueprint(VERSION_ONE)

    return app
