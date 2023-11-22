import os
from dotenv import load_dotenv
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import base64

load_dotenv('app.env')

# Load and decode AES key and IV from environment variables
AES_KEY_BASE64 = os.environ.get("AES_KEY")
IV_BASE64 = os.environ.get("IV")

if AES_KEY_BASE64 is None or IV_BASE64 is None:
    raise ValueError("Error: AES_KEY or IV is not set. Please set them in the app.env file.")

# Remove any unnecessary characters (e.g., newline characters) from the base64-encoded strings
AES_KEY_BASE64 = AES_KEY_BASE64.strip()
IV_BASE64 = IV_BASE64.strip()

# Decode the base64-encoded key and IV to bytes
AES_KEY = base64.b64decode(AES_KEY_BASE64)
IV = base64.b64decode(IV_BASE64)

# Ensure the key is 32 bytes (256 bits) and IV is 16 bytes (128 bits)
if len(AES_KEY) != 32 or len(IV) != 16:
    raise ValueError("Error: AES_KEY should be 32 bytes long, and IV should be 16 bytes long.")

backend = default_backend()

def encrypt_message(message):
    cipher = Cipher(algorithms.AES(AES_KEY), modes.CFB(IV), backend=backend)
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(message.encode()) + encryptor.finalize()
    return ciphertext

def decrypt_message(encrypted_message):
    cipher = Cipher(algorithms.AES(AES_KEY), modes.CFB(IV), backend=backend)
    decryptor = cipher.decryptor()
    decrypted_message = decryptor.update(encrypted_message) + decryptor.finalize()
    return decrypted_message.decode()

# Example usage
user_message = "Hello, chatbot! This is a test message."

# Encryption
encrypted_message = encrypt_message(user_message)
print("Encrypted Message:", base64.b64encode(encrypted_message).decode())

# Decryption
decrypted_message = decrypt_message(encrypted_message)
print("Decrypted Message:", decrypted_message)

# Decryption front end
# encrypted_message_2 = "U2FsdGVkX1/yr80GZhvjGPLHt44GW5/RlErUXLgDfNiMxVumhXRkQwcjMMVqwQ0vi51JaI4HurOE/XxGBBhOow=="
# # Ensure the input is of type bytes
# encrypted_message_2_bytes = base64.b64decode(encrypted_message_2)

# # Adjust the encryption algorithm and mode based on the information from the frontend
# decrypted_message_2 = decrypt_message(encrypted_message_2_bytes)
# print("Decrypted Message:", decrypted_message_2)