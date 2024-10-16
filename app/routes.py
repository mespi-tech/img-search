from flask import Flask
from app.repository.user_repository import UserRepository
from app.repository.order_repository import OrderRepository
from app.usecase.user_service import UserService
from app.controller.user_controller import UserController

def init_routes(app: Flask):
    # Init repository and service

    user_repository = UserRepository()
    order_repository = OrderRepository()
    user_service    = UserService(user_repository, order_repository)
    user_controller = UserController(user_service)
    # defind route

    app.add_url_rule('/users', view_func=user_controller.get_users, methods=['GET'])
    app.add_url_rule('/users', view_func=user_controller.create_user, methods=['POST'])
    app.add_url_rule('/user-order', view_func=user_controller.create_user_order, methods=['POST'])
