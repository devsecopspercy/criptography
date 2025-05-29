from cryptography.fernet import Fernet


# Write and save a encryption key
def generate_key():
    the_key = Fernet.generate_key()
    with open("my_key.key", "wb") as key_file:
        key_file.write(the_key)


# Load the encryption key
def load_key():
    return open("my_key.key", "rb").read()


# ---------------------------Encrypt a message----------#
generate_key() 
my_key = load_key()

# Example message to encrypt
message = "Hello, this is a secret message!".encode()

#
fernet = Fernet(my_key)

encrypted_message = fernet.encrypt(message)
print("Encrypted message:", encrypted_message)


# Decrypt the message
decrypted_message = fernet.decrypt(encrypted_message)
print("Decrypted message:", decrypted_message.decode())






