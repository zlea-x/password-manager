from cryptography.fernet import Fernet
import os

class EncryptionUtil:
    KEY_FILE = "secret.key"

    @staticmethod
    def generate_key():
        key = Fernet.generate_key()
        with open(EncryptionUtil.KEY_FILE, "wb") as key_file:
            key_file.write(key)

    @staticmethod
    def load_key():
        if not os.path.exists(EncryptionUtil.KEY_FILE):
            EncryptionUtil.generate_key()
        with open(EncryptionUtil.KEY_FILE, "rb") as key_file:
            return key_file.read()
        
    @staticmethod
    def encrypt(data: str) -> bytes:
        key = EncryptionUtil.load_key()
        return Fernet(key).encrypt(data.encode())
    
    @staticmethod
    def decrypt(token: bytes) -> str:
        key = EncryptionUtil.load_key()
        return Fernet(key).decrypt(token).decode()
    
    