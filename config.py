import os
from dotenv import load_dotenv

load_dotenv('app.env')

SECRET_KEY = os.environ.get('OPENAI_API_KEY') 
if SECRET_KEY is None:
    raise ValueError("OPENAI_API_KEY is not set. Please set it in the .env file.")

AES_KEY = os.environ.get("AES_KEY")
if AES_KEY is None:
    raise ValueError("Error: AES_KEY is not set. Please set it in the .env file.")

if len(AES_KEY) != 32:
    raise ValueError("Error: AES_KEY should be 32 bytes long.")


DEBUG = True