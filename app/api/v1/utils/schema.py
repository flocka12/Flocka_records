''' module for validating inputs '''
from marshmallow import Schema, fields

class UserSchema(Schema):
    ''' class to validate user fields '''
    firstname = fields.Str(required=True)
    lastname = fields.Str(required=True)
    email = fields.Str(required=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True)
    