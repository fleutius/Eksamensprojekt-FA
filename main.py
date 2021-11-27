import os
import hashlib

##Design Fase 

#Requerements list:
# Register users in a text file 
# look for textfiles: initialer:navn:email:password:profil
# Initialer: Maks 4 tegn der identificerer brugeren (Primary Key)
# navn: Brugerens navn "Fornavn Efternavn" ---string
# email: brugers email string med email - ligesom initialer er dette en identifikationsfaktor (primary key)
#password: Hash af et indtastet password -
# profil: encifret kode mellem 1-6 .Bruges til at tillade eller forhindre adgang til systemer (access level)


# IDEER: F
"""
sdasd
Bruger class
data class?
profil kan være en selectable
Text file

UNDERSØGES::::::::
Selectable variables
python hashing

"""
def email():
    try:
        email_in = input("Please enter Users")
        if "@" and "." in email_in:
            return email_in
        else: raise ValueError
    except ValueError:
        print("please enter a correct email. ")
        email()
class User:
    users = []
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.name = (first_name + ' ' + last_name)
        self.email = email
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



    def create_user():
        user=User(
            first_name = input("Please enter Users first name: "),
            last_name = input("Please enter Users last name: "),
            email = email()
        )


User.create_user()