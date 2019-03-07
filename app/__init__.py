''' module for creating app '''
from flask import Flask
from .api.v1 import version_one

def create_app:
    app = Flask(__name__)
    app.register_blueprint(version_one)

    return app