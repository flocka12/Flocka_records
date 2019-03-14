''' module for creating and registering endpoints '''
from flask import Blueprint
from flask_restful import Api
from .views.user_view import UserRegistration, Userlogin, UserProfile
from .views.music_view import MusicList

VERSION_ONE = Blueprint('api_v1', __name__, url_prefix='/api/v1')

API = Api(VERSION_ONE)
API.add_resource(UserRegistration, '/auth/signup')
API.add_resource(Userlogin, '/auth/login')
API.add_resource(UserProfile, '/auth/user/profile')
API.add_resource(MusicList, '/auth/user/music')
