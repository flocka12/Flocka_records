''' module for creating and registering endpoints '''
from flask import Blueprint
from flask_restful import Api

VERSION_ONE = Blueprint('api_v1', __name__, url_prefix='/api/v1')

API = Api(VERSION_ONE)
