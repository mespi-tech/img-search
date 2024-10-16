from app.repository.abstract_user_repository import AbstractUserRepository
from app.usecase.abstract_user_service import AbstractUserService

class UserService(AbstractUserService):

    def __init__(self, user_repository: AbstractUserRepository):
        self.user_repository = user_repository

    def get_all_users(self):
        return self.user_repository.get_all_users()

    def create_user(self, data: dict):
        return self.user_repository.create_user(data)
