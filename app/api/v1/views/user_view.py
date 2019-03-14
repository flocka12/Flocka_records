''' module representing the user view '''
from flask_restful import Resource, request
from flask_jwt_extended import (
    jwt_required, create_access_token, create_refresh_token,
    get_jwt_identity
)
from app.api.v1.models.user_model import User
from app.api.v1.utils.schema import UserSchema

class UserRegistration(Resource):
    ''' creates a user in the database '''
    def __init__(self):
        self.data_base = User()
    def post(self):
        ''' adds  user to the user list '''
        data, errors = UserSchema().load(request.get_json())

        if errors:
            return errors

        if self.data_base.find_if_exists('username', data['username']):
            return 'username already taken'
        if self.data_base.find_if_exists('email', data['email']):
            return  'email already in use'

        user = {
            'firstname': data['firstname'],
            'lastname': data['lastname'],
            'email': data['email'],
            'username': data['username'] if data['username'] else data['email'],
            'password': data['password'],
        }

        user = self.data_base.add_user(user)

        response = UserSchema(exclude=['password']).dump(user)[0]
        return {
            'data': response,
            'message': 'Successfully created user'
            }
class Userlogin(Resource):
    ''' define user login '''
    def __init__(self):
        self.data_base = User()
    def post(self):
        ''' logins user '''
        data, errors = UserSchema(only=('username', 'password')).load(request.get_json())

        if errors:
            return errors

        users = self.data_base.for_where('username', data['username'])

        if not users:
            return 'not users'
        user = users[0]

        return {
            'access_token': create_access_token(UserSchema(exclude=['password']).dump(user)[0],
                                                expires_delta=False),
            'refresh_token': create_refresh_token(UserSchema(exclude=['password']).dump(user)[0]),
            'user': user,
            'message': 'Successfully login'
        }
class UserProfile(Resource):
    ''' Define User Profile with authorization'''
    @jwt_required
    def get(self):
        ''' get user by token '''
        user = get_jwt_identity
        return user
