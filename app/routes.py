from app import app
from app.bot import get_response

@app.route('/')
def hello_world():
    return 'Hello, World!'

# Route with prompt for the chatbot goes here
