# src/core/interfaces/user_interface.py
from abc import ABC, abstractmethod
from src.domain.entities.user import User
from datetime import datetime, timedelta

class UserInterface(ABC):
    @abstractmethod
    def save_data(self, user_id: str, session_id: str, session_data):
        pass

    @abstractmethod
    def check_user(self, membername, memberpass):
        pass

    @abstractmethod
    def get_user_data(self, member_id: str):
        pass
    
    @abstractmethod
    def get_all_sessions(self, user_id:str):
        pass

    
   




