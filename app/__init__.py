''' module for creating app '''
import settings
from flask import Flask
from flask_jwt_extended import JWTManager
from instance.config import APP_CONFIG
from DB.db_con import db_init
from .api.v1 import VERSION_ONE

def create_app(config_name):
    ''' creates app and registers blueprints '''
    app = Flask(__name__)
    db_init()
    JWTManager(app)
    app.register_blueprint(VERSION_ONE)
    app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
    app.config.from_pyfile('..\\instance\\config.py')
    return app
