
import os
import hashlib

class User:
    '''File handling part'''
    
    
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
        self.user_file = open("user_file.txt", "a")
        lines = f"{self.initials} - {self.name} - {self.email} - {self.access_level} - {self.key}\n" 
        self.user_file.writelines(str(lines))
        self.user_file.close()


    def file_read():
        with open("user_file.txt", 'r') as f:
            read_file = f.readlines()
            for line in read_file:
                wordInLine = line.split("-")
                print(f"Initialer: {wordInLine[0]}\nNavn: {wordInLine[1]}\nEmail: {wordInLine[2]}\nprofil: {wordInLine[3]}\nHashed Kode: {wordInLine[4]}")

    def fffd():
        f= open("user_file.txt","r")
        print(f)



User.file_read()