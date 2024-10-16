from flask import Flask
from app.repository.user_repository import UserRepository
from app.usecase.user_service import UserService
from app.controller.user_controller import UserController
from app.entity import db

def init_routes(app: Flask):
    # Init repository and service

    user_repository = UserRepository(db)
    user_service    = UserService(user_repository)
    user_controller = UserController(user_service)
    # defind route

    app.add_url_rule('/users', view_func=user_controller.get_users, methods=['GET'])
    app.add_url_rule('/users', view_func=user_controller.create_user, methods=['POST'])
