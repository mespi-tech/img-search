from abc import ABC, abstractmethod
from typing import List
from app.entity.user import User

class AbstractUserRepository(ABC):

    @abstractmethod
    def get_all_users(self) -> List[User]:
        pass

    @abstractmethod
    def create_user(self, data: dict) -> User:
        pass
