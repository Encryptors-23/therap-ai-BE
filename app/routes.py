from app import app
# test_respose is a hardcoded response for testing purposes
from app.bot import get_response, test_response
from flask import request, jsonify

@app.route('/')
def hello_world():
    return 'Hello, World!'

# Route with prompt for the chatbot goes here
@app.route('/bot', methods=['POST'])
def bot_response():
    prompt = request.json['prompt']
    response = test_response(prompt)
    #return jsonify({'response': response})
    return jsonify(response)
