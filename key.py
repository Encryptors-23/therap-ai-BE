import os
import base64

# Generate a random 32-byte key
aes_key = os.urandom(32)

# Encode the key in Base64 format for storage
aes_key_base64 = base64.b64encode(aes_key).decode()

# Print the key
print("Generated AES Key:", aes_key_base64)

# Save the key to the .env file
with open('app.env', 'w') as env_file:
    env_file.write(f'AES_KEY="{aes_key_base64}"')
