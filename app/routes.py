from app import app
from app.bot import get_response
from flask import request, jsonify

# Route with prompt for the chatbot goes here
@app.route('/bot', methods=['POST'])
def bot_response():
    prompt = request.json['prompt']
    response = get_response(prompt)
    return jsonify({'response': response})
