#the main file that runs the program

#PasswordEntry test
from password_entry import PasswordEntry

def main():
    entry = PasswordEntry("github.com", "zlea-joycrate", "Firstclass5.0")
    print(entry.to_dict()) #prints the dictionary version

     # Save the entry to a file
    data = entry.to_dict()
    loaded_entry = PasswordEntry.from_dict(data) 
    print(loaded_entry.website, loaded_entry.username, loaded_entry.password) #prints the loaded entry

if __name__ == "__main__":
    main()

#Encryption test
from encryption_util import EncryptionUtil
def test_encryption():
    text = "Firstclass5.0"
    encrypted = EncryptionUtil.encrypt(text)
    print ("Encrypted:", encrypted)

    decrypted = EncryptionUtil.decrypt(encrypted)
    print ("Decrypted:", decrypted)

if __name__ == "__main__":
    test_encryption()

#PasswordManager test
from password_entry import PasswordEntry
from password_manager import PasswordManager

def main():
    manager = PasswordManager()

    #Adding a new password
    entry = PasswordEntry("Amazon.com", "anuri_mena", "welov3shopp1ng")
    manager.add_password(entry)

    #getting the password
    result = manager.get_password("Amazon.com")
    if result:
        print(f"Found: {result.website} - {result.username} - {result.password}")
    else:
        print("Not found")

    result = manager.get_password("Zara.com")
    if result:
        print(f"Found: {result.website} - {result.username} - {result.password}")
    else:
        print("Not found")

    