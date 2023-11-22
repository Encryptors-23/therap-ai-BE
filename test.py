import os
from dotenv import load_dotenv
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import base64

# Load environment variables from app.env
load_dotenv('app.env')

# Load and decode AES key from environment variable
AES_KEY_BASE64 = os.environ.get("AES_KEY")
if AES_KEY_BASE64 is None:
    raise ValueError("Error: AES_KEY is not set. Please set it in the app.env file.")

# Remove any unnecessary characters (e.g., newline characters) from the base64-encoded string
AES_KEY_BASE64 = AES_KEY_BASE64.strip()

# Decode the base64-encoded key to bytes
AES_KEY = base64.b64decode(AES_KEY_BASE64)

# # Ensure the key is 32 bytes (256 bits)
if len(AES_KEY) != 32:
    raise ValueError("Error: AES_KEY should be 32 bytes long.")

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

# Example usage
user_message = "Hello, chatbot! This is a test message."

# Encryption
encrypted_message = encrypt_message(user_message)
print("Encrypted Message:", encrypted_message)

# Decryption
decrypted_message = decrypt_message(encrypted_message)
print("Decrypted Message:", decrypted_message)
