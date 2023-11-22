import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.environ.get('OPENAI_API_KEY') 
if SECRET_KEY is None:
    raise ValueError("OPENAI_API_KEY is not set. Please set it in the .env file.")
DEBUG = True