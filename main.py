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


from encryption_util import EncryptionUtil
def test_encryption():
    text = "Firstclass5.0"
    encrypted = EncryptionUtil.encrypt(text)
    print ("Encrypted:", encrypted)

    decrypted = EncryptionUtil.decrypt(encrypted)
    print ("Decrypted:", decrypted)

if __name__ == "__main__":
    test_encryption()
