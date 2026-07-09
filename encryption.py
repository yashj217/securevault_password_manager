import os
from cryptography.fernet import Fernet

KEY_FILE = "data/secret.key"
def generate_key():
 #print("generate_key() called")
   #Generates a new Fernet key if it does not already exist.
 if not os.path.exists(KEY_FILE):
  #print("creating key..")
  key = Fernet.generate_key()
  with open(KEY_FILE, "wb") as file:
   file.write(key)
  # print("key creye successfullyy!!")

def load_key():
 generate_key()
 with open(KEY_FILE , "rb") as file:
  return file.read()
    
def encrypt_password(password):
 key = load_key()
 cipher = Fernet(key)   
 encrypted_password = cipher.encrypt(password.encode())
 return encrypted_password.decode()

def decrypt_password(encrypted_password):
 key = load_key()
 cipher = Fernet(key)
 decrypted_password = cipher.decrypt(encrypted_password.encode())
 return decrypted_password.decode()


if __name__ =="__main__":
 sample = "maypssword@23"
 encrypted = encrypt_password(sample)
 decrypted = decrypt_password(encrypted)
 print("Original :", sample)
 print("Encrypted:", encrypted)
 print("Decrypted:", decrypted)