'''
Eksamensprojekt-FA Python program af Flemming Kærgaard. 
Bemærk, programmet opretter en text fil kaldet 'user_file.txt' i samme direktory som programmet køres fra. Denne fil er nødvendig for funktionaliteten af programmet.
'''

# sys importeres for at give exit funktionalitet
from classes import User
import checks
import sys

# Hvis ikke "user_file.txt" findes i mappen hvor programmet køres fra, oprettes denne fil. 


# create_user() laver instance af User class fra Classes.py ud fra input fra brugeren. Disse input håndteres i nogle instanser af Checks.py for at sikre at det indtastede overholder de givne kriterier for opgaven.
# Herefter benyttes user_registration fra Classes.py til at indføre instance i text filen.
def create_user():
    user=User(
        initials = checks.initials_check(),
        first_name = input("Please enter Users first name: "),
        last_name = input("Please enter Users last name: "),
        email = checks.email_check(),
        access_level = checks.access_check(),
    )
    user.user_registration()
    contenue()

# contenue() muligtgører det for brugeren at fortsætte med at bruge programmet, selv efter den valgte funktionalitet er gennemført. 
def contenue():
    print("Would you like to contenue? ")
    print("1 - Yes, from the start. ")
    print("2 - Yes, from user registration. ")
    print("3 - No, end the program. ")
    selection = input("Please enter selection ")   
    if selection == "1":
        start_menu()
    elif selection == "2":
        create_user()
    elif selection == "3":
        sys.exit
    else:
        print("Please enter either 1, 2 or 3.. ")
        contenue()

# start_menu() er brugerens umiddelbare første niveau for interaktion. Det her fra at bruger vælger hvad der skal gøres.
def start_menu():
    print("What do you wish to do? ")
    print("1 - Register new user into the system. ")
    print("2 - View all registered users. ")
    selected = input("Please enter 1 / 2, for desired functionality. ")
    
    if selected == "1":
        print("You have selected user registration. ")
        create_user()
        contenue()
    if selected == "2":
        print("You have selected to view all registered users. ")
        User.file_read()
        contenue()
    else:
        print("Please enter either 1 or 2 to select functionality.. ")
        start_menu()
        
# main()'s eneste funktion er at informere kort om at der oprettes en text fil, og oprette samme text  fil, herefter videresendes bruger til start_menu()
def main():
    open("user_file.txt", "a")
    print()
    print("Welcome to the user management system. ")
    print("Please beware, that the program creates a file called user_file.txt in the same directory as the program is running in. ")
    print()
    start_menu()




main()