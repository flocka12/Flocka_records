''' module representing the music view '''
from flask_restful import Resource
from flask_jwt_extended import jwt_required

from app.api.v1.models.music_model import Music

class MusicList(Resource):
    """Represents a resource class used to interact with Music through through HTTP methods."""

    def __init__(self):
        """Initialize resource with a reference to the model it should use."""

        self.data_base = Music()

    @jwt_required
    def get(self):
        """Fetch a list of all records from the model."""

        data = self.data_base.all()

        return data
        