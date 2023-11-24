from base64 import b64decode, b64encode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad

# The secret key and IV used in the frontend - you can put them in an .env file, but remember to use b64decode() here
secret_key = b64decode("vl/VxRuThkD+v+9S7twDR/eT9v+mye2EvaF4ojeRhTM=")
iv = b64decode("PynS/ydkhb2EUMzVty9sww==")

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