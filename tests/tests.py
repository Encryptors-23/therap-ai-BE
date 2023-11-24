from app.encryption import encrypt, decrypt
import base64

def test_encryption_decryption():
    user_message = "Hello, chatbot! This is a test message."

    # Encryption
    encrypted_message = encrypt(user_message)
    # print("Encrypted Message:", base64.b64encode(encrypted_message).decode())
    assert isinstance(encrypted_message, str)
    # Decryption
    decrypted_message = decrypt(encrypted_message)
    assert decrypted_message == user_message
    # print("Decrypted Message:", decrypted_message)







# Tests
# @app.route('/test', methods=['POST'])
# def test_encryption():
#     user_message = "Hello, chatbot! This is a test message."
#     response = app.test_client().post('/bot', json={'prompt': user_message})
#     encrypted_bot_response = response.json['encrypted_response']
#     bot_response = decrypt_message(encrypted_bot_response)
#     return jsonify({'user_message': user_message, 'bot_response': bot_response})