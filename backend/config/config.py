# sample config file

from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

SECRET_KEY=os.getenv('SECRET_KEY')
HOST=os.getenv('HOST')
DBNAME=os.getenv('DBNAME')
USER=os.getenv('USER', "vaadminevva")
PASSWORD=os.getenv('PASSWORD')
CONNECTION_STRING=os.getenv('CONNECTION_STRING')


OPENAI_API_KEY=os.getenv('OPENAI_API_KEY')
