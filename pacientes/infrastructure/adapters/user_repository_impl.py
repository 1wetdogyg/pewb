# infrastructure/adapters/user_repository_impl.py

from typing import List, Optional
from uuid import uuid4
from domain.usuario import User, UserCreate, UserUpdate
from application.ports.user_repository import UserRepository


class UserRepositoryImpl(UserRepository):

    def __init__(self):
        self.users: List[User] = []

    def save(self, user_data: UserCreate) -> User:
        new_user = User(
            id=str(uuid4()),
            username=user_data.username,
            email=user_data.email
        )
        self.users.append(new_user)
        return new_user

    def find_by_id(self, user_id: str) -> Optional[User]:
        for user in self.users:
            if user.id == user_id:
                return user
        return None

    def find_by_email(self, email: str) -> Optional[User]:
        for user in self.users:
            if user.email == email:
                return user
        return None

    def find_all(self) -> List[User]:
        return self.users

    def update(self, user_id: str, user_update: UserUpdate) -> Optional[User]:
        user = self.find_by_id(user_id)
        if not user:
            return None

        if user_update.username is not None:
            user.username = user_update.username

        if user_update.email is not None:
            user.email = user_update.email

        if user_update.status is not None:
            user.status = user_update.status

        return user

    def delete(self, user_id: str) -> bool:
        user = self.find_by_id(user_id)
        if not user:
            return False

        self.users.remove(user)
        return True
