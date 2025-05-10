#import 
import json
import os
from password_entry import PasswordEntry
from encryption_util import EncryptionUtil

class PasswordManager:
    def __init__(self, filename="passwords.json"): # initializes passwordmanager and saves data here
        self.filename = filename
        self.passwords = []  # list that'll store the password entries
        self.load_from_file() # loads any existing saved passwords from the file

    def add_password(self, entry: PasswordEntry):
        """
        Add a new password entry objest to the manager.
        """
        self.passwords.append(entry)
        self.save_to_file()
