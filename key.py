import base64
import secrets

# Generate a random 32-byte key and convert to Base64
aes_key = secrets.token_bytes(32)
aes_key_base64 = base64.b64encode(aes_key).decode()

# Generate a random 16-byte IV and convert to Base64
iv = secrets.token_bytes(16)
iv_base64 = base64.b64encode(iv).decode()

print("Generated AES Key:", aes_key_base64)
print("Generated IV:", iv_base64)

# Save the key and IV to the .env file
with open('.env', 'w') as env_file:
    env_file.write(f'AES_KEY="{aes_key_base64}"\n')
    env_file.write(f'IV="{iv_base64}"\n')
