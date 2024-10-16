from abc import ABC, abstractmethod

class AbstractUserService(ABC):

    @abstractmethod
    def get_all_users(self):
        pass

    @abstractmethod
    def create_user(self, data: dict):
        pass
