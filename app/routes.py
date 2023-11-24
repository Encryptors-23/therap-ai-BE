from app import app
# test_respose is a hardcoded response for testing purposes
from app.bot import get_response, test_response
from flask import request, jsonify
from app.encryption import encrypt, decrypt 
import os 


# Base request without encryption
# Route with prompt for the chatbot goes here
# @app.route('/bot', methods=['POST'])
# def bot_response():
#     prompt = request.json['prompt']
#     response = test_response(prompt)
#     #return jsonify({'response': response})
#     return jsonify(response)



# Route with prompt for the chatbot goes here
@app.route('/bot', methods=['POST'])
def bot_response():
    prompt = request.json['prompt']
    encrypted_user_prompt = encrypt_message(prompt)
    decrypted_user_prompt = decrypt_message(encrypted_user_prompt)
    bot_response = test_response(decrypted_user_prompt)
    encrypted_bot_response = encrypt_message(bot_response)
    #return jsonify({'response': response})
    return jsonify({'encrypted_response': encrypted_bot_response})
    # return jsonify(response)




