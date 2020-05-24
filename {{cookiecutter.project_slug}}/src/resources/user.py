from flask import request, jsonify
from flask_restful import Resource

from repositories import UserRepository


class User(Resource):
    def get(self, username: str):
        # TODO: error handler
        # move to another resource
        user = UserRepository.get(username)
        return user, 200


class UserList(Resource):
    def post(self):
        """
        Create user
        """
        request_json = request.get_json(silent=True)
        username: str = request_json['username']
        avatar_url: str = request_json.get('avatar_url', '')
        try:
            user = UserRepository.create(username, avatar_url)
            return user, 200
        except Exception as e:
            response = jsonify(e.to_dict())
            response.status_code = e.status_code
            return response
