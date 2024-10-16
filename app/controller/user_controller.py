from flask import jsonify, request
from app.usecase.abstract_user_service import AbstractUserService

class UserController:

    def __init__(self, user_service: AbstractUserService):
        self.user_service = user_service
    
    def get_users(self):
        users = self.user_service.get_all_users()
        return jsonify([user.json() for user in users])

    def create_user(self):
        data = request.get_json()
        new_user = self.user_service.create_user(data)
        return jsonify(new_user.json()), 201
