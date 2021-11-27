def email_check():
    try:
        email_in = input("Please enter Users e-mail: ")
        if "@" and "." in email_in:
            return email_in
        else: raise ValueError
    except ValueError:
        print("please enter a valid e-mail. ")
        email()

def initials_check():
    try:
        initials_in = input("Please enter Users initials  (max 4 characters) ")
        if not isinstance(initials_in, str):
            raise TypeError
        elif len(initials_in) > 4:
            raise ValueError
        else: 
            return initials_in
    except TypeError:
        print("please enter initials with letters only. ")
        initials_check()
    except ValueError:
        print("Max 4 characters. ")
        initials_check()

def access_check():
    try:
        access_in = input("Please enter Users Access level  (1-6) ")
        if not isinstance(access_in, int):
            raise TypeError
        elif not len(access_in) == 1:
            raise ValueError
        else: 
            return access_in
    except TypeError:
        print("please enter access level using a number. ")
        access_check()
    except ValueError:
        print("Access level is single digit. ")
        access_check()    

