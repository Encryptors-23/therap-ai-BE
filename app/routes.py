from app import app
# test_respose is a hardcoded response for testing purposes
from app.bot import get_response, test_response
from flask import request, jsonify
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os 

backend = default_backend()

def encrypt_message(message):
    # Generate a random IV (Initialization Vector) for each encryption
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(AES_KEY), modes.CFB(iv), backend=backend)
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(message.encode()) + encryptor.finalize()
    return iv + ciphertext

def decrypt_message(encrypted_message):
    iv = encrypted_message[:16]
    ciphertext = encrypted_message[16:]
    cipher = Cipher(algorithms.AES(AES_KEY), modes.CFB(iv), backend=backend)
    decryptor = cipher.decryptor()
    decrypted_message = decryptor.update(ciphertext) + decryptor.finalize()
    return decrypted_message.decode()


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

# Tests
@app.route('/test', methods=['POST'])
def test_encryption():
    user_message = "Hello, chatbot! This is a test message."
    response = app.test_client().post('/bot', json={'prompt': user_message})
    encrypted_bot_response = response.json['encrypted_response']
    bot_response = decrypt_message(encrypted_bot_response)
    return jsonify({'user_message': user_message, 'bot_response': bot_response})


