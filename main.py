from Classes import User
import checks
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
#----------------------------------------------------------------
# TODO:
# Add Text file to
# Integrate text file:
#----------------------------------------------------------------

def create_user():
    user=User(
        initials = checks.initials_check(),
        first_name = input("Please enter Users first name: "),
        last_name = input("Please enter Users last name: "),
        email = checks.email_check(),
        access_level = checks.access_level_check(),
    )


User.create_user()