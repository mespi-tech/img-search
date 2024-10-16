from typing import List

from flask_sqlalchemy import SQLAlchemy
from app.repository.abstract_user_repository import AbstractUserRepository
from app.entity.user import User

class UserRepository(AbstractUserRepository):

    def __init__(self, db: SQLAlchemy):
        self.db = db

    def get_all_users(self) -> List[User]:
        return User.query.all()

    def create_user(self, data: dict) -> User:
        new_user = User(name=data['name'], email=data['email'])
        self.db.session.add(new_user)
        self.db.session.commit()
        return new_user
