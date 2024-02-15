# sample config file

from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

SECRET_KEY=os.getenv('SECRET_KEY')

SQL_DB_URL=os.getenv('SQL_DB_URL')

OPENAI_API_KEY=os.getenv('OPENAI_API_KEY')
