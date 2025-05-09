class PasswordEntry:
    def __init__(self, website, username, password):
        self.website = website
        self.username = username
        self.password = password

    def to_dict(self):
        return {
            "website": self.website,
            "username": self.username,
            "password": self.password
        }

    @staticmethod
    def from_dict(data):
        return PasswordEntry(
            data["website"],
            data["username"],
            data["password"]
        )
        
