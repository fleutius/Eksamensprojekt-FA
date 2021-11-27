import os
import hashlib

class User:
    users = []
    def __init__(self,initials ,first_name, last_name, email, access_level):
        self.initials = initials
        self.first_name = first_name
        self.last_name = last_name
        self.name = (first_name + ' ' + last_name)
        self.email = email
        self.access_level = access_level
        self.salt = os.urandom(32)
        self.password = input("Please enter your password: ")
        self.key = hashlib.pbkdf2_hmac(
            'sha256',
            self.password.encode('utf8'),
            self.salt,
            100000,
            dklen=128
        )
        self.storedpass = self.salt + self.key
        self.password = ''
        self.users.append(self.email)