''' module representing the user view '''
from flask_restful import Resource, request
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
        