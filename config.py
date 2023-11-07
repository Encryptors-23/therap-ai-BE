import os

SECRET_KEY = os.environ.get('SECRET_KEY') 
if SECRET_KEY is None:
    raise ValueError("SECRET_KEY is not set. Please set it as an environment variable.")
DEBUG = True
