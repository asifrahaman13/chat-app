from config.config import SECRET_KEY
from langchain_openai import OpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
import os
from config.config import OPENAI_API_KEY
import os


class ChatRepository:

    def __init__(self):
        self.api_key = OPENAI_API_KEY
        self.memory = ConversationBufferMemory(return_messages=True)
        self.memory.save_context({"input": "hi"}, {"output": "whats up"})
        self.llm = OpenAI(temperature=0, api_key=self.api_key)
        self.conversation = ConversationChain(llm=self.llm, verbose=True, memory=ConversationBufferMemory())

    def chat_response(self, question):
        # response = self.conversation.predict(input=question)
        response = "In this implementation, the UserSessionData and UserData classes are defined as SQLModel classes with appropriate relationships. The save_data method uses a SQLModel Session to interact with the database. It checks if a user with the given user_id exists. If the user exists, it appends a new UserSessionData instance to the sessions list. If the user does not exist, it creates a new UserData instance with the UserSessionData instance in the sessions list and adds it to the session for insertion into the database. Finally, it commits the changes to the database."
        return response
