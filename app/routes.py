from app import app
from app.bot import get_response
from flask import request, jsonify
from app.encryption import encrypt, decrypt 

# Route with prompt for the chatbot goes here
@app.route('/bot', methods=['POST'])
def bot_response():
    encrypted_user_prompt = request.json['prompt']
    decrypted_user_prompt = decrypt(encrypted_user_prompt)
    bot_response = get_response(decrypted_user_prompt)
    encrypted_bot_response = encrypt(bot_response)
    return jsonify({'encrypted_response': encrypted_bot_response})




