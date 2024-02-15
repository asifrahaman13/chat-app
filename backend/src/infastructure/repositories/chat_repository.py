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
        response = self.conversation.predict(input=question)

        return response
