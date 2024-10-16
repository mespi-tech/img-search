from app.repository.abstract_user_repository import AbstractUserRepository
from app.repository.abstract_order_repository import AbstractOrderRepository
from app.usecase.abstract_user_service import AbstractUserService

class UserService(AbstractUserService):

    def __init__(self, user_repository: AbstractUserRepository, order_repository: AbstractOrderRepository):
        self.user_repository    = user_repository
        self.order_repository   = order_repository

    def get_all_users(self):
        return self.user_repository.get_all_users()

    def create_user(self, data: dict):
        return self.user_repository.create_user(data)

    def create_user_order(self, data: dict):
        new_user = self.user_repository.create_user(data)
        new_order = self.order_repository.create_order(data)
        return new_user
