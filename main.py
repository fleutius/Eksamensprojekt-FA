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

class Bruger:
    
    def __init__(self, first_name, last_name, email, password, profil):
        self.name = self.first_name + ' ' + self.last_name
        self.email = email
        self.password = password
        self.profil = profil

    

