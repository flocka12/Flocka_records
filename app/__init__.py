''' module for creating app '''
from flask import Flask
from flask_jwt_extended import JWTManager
from instance.config import APP_CONFIG
from DB.queries import create_tables
from .api.v1 import VERSION_ONE

def create_app(config_name):
    ''' creates app and registers blueprints '''
    app = Flask(__name__)
    create_tables()
    JWTManager(app)
    app.register_blueprint(VERSION_ONE)
    app.config.from_object(APP_CONFIG[config_name])

    return app
