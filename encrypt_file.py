from cryptography.fernet import Fernet

def load_key():
    """Load the encryption key from a file."""
    return open("my_key.key", "rb").read()

# Encrypt function
def encrypt_file(file_name, key):
   fernet = Fernet(key)
   with open(file_name, "rb") as file:
       file_info = file.read()
       encrypted_data = fernet.encrypt(file_info)
   with open(file_name + ".encrypted", "wb") as encrypted_file:
        encrypted_file.write(encrypted_data)

# Decrypt function
def decrypt_file(file_name, key):
    fernet = Fernet(key)
    with open(file_name, "rb") as encrypted_file:
        encrypted_data = encrypted_file.read()
        decrypted_data = fernet.decrypt(encrypted_data)
    with open(file_name, "wb") as decrypted_file:
        decrypted_file.write(decrypted_data)

#-----------------------Encript a file------------------#
my_key = load_key()
one_file = "my_file.txt"  # Replace with your file name
encrypt_file(one_file, my_key)

#-----------------------Decrypt a file------------------#
decrypt_file(one_file + ".encrypted", my_key)