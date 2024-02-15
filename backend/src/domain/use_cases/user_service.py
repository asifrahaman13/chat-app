# src/core/use_cases/user_service.py


from src.domain.interfaces.user_interface import UserInterface
from src.infastructure.repositories.user_repository import UserRepository
from fastapi.security import OAuth2PasswordBearer
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class UserService(UserInterface):
    def __call__(self) -> UserInterface:
        return self

    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def save_data(self, user_id, session_id, session_data):
        return self.user_repository.save_data(user_id, session_id, session_data)

    def check_user(self, membername: str, memberpass: str) -> bool:
        return self.user_repository.check_user(membername, memberpass)

    def get_user_data(self, member_id: str):
        return self.user_repository.get_user_data(member_id)

    def get_all_sessions(self, user_id: str):
        return self.user_repository.get_all_sessions(user_id)

    def save_user(self, membername: str, memberpass: str):
        return self.user_repository.save_user(membername, memberpass)
