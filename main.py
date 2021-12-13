from classes import User
import checks
import sys

open("user_file.txt", "a")

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


def start_menu():
    print("What do you wish to do? ")
    print("1 - Register new user into the system. ")
    print("2 - View all registered users. ")
    selected = input("Please enter 1 / 2, for desired functionality. ")
    
    if selected == "1":
        print("You have selected user registration. ")
        create_user()
    if selected == "2":
        print("You have selected to view all registered users. ")
        User.file_read()
        contenue()
    else:
        print("Please enter either 1 or 2 to select functionality.. ")
        start_menu()
        print()

User.file_read()

def main():
    print()
    print("Welcome to the user management system. ")
    print("Please beware, that the program creates a file called user_file.txt in the same directory as the program is running in. ")
    print()
    start_menu()




main()