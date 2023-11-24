from base64 import b64decode, b64encode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
from config import AES_KEY, IV


# The secret key and IV are in an .env file, which is not included in the repo.
secret_key = b64decode(AES_KEY)
iv = b64decode(IV)

def decrypt(hash):
    ciphertext = b64decode(hash)
    cipher = AES.new(secret_key, AES.MODE_CBC, iv=iv)

    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return plaintext.decode('utf-8')

def encrypt(plaintext):
    plaintext_bytes = pad(plaintext.encode('utf-8'), AES.block_size)
    cipher = AES.new(secret_key, AES.MODE_CBC, iv=iv)

    ciphertext = b64encode(cipher.encrypt(plaintext_bytes))
    return ciphertext.decode('utf-8')

