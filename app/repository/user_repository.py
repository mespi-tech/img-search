from typing import List
from app.entity import db
from app.repository.abstract_user_repository import AbstractUserRepository
from app.entity.user import User

class UserRepository(AbstractUserRepository):

    def get_all_users(self) -> List[User]:
        return User.query.all()

    def create_user(self, data: dict) -> User:
        new_user = User(name=data['name'], email=data['email'])
        db.session.add(new_user)
        return new_user
