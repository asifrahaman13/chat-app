from src.domain.interfaces.chat_interface import ChatInterface
from src.infastructure.repositories.chat_repository import ChatRepository
from fastapi.security import OAuth2PasswordBearer
from fastapi.security import OAuth2PasswordBearer
from src.infastructure.repositories.chat_repository import ChatRepository

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class ChatService(ChatInterface):
    def __call__(self) -> ChatInterface:
        return self

    def __init__(self, chat_repository: ChatRepository):
        self.chat_respository = chat_repository

    def chat_response(self, question):
        return self.chat_respository.chat_response(question)
