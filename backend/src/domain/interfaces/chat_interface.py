# src/core/interfaces/user_interface.py
from abc import ABC, abstractmethod


class ChatInterface(ABC):
    
    @abstractmethod
    def chat_response(self, question):
        pass