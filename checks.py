# email_check beder om brugers input til email. Herefter vurderes der i try, om emailen indeholder  både et "@" og et "."
# hvis der findes fejl, godtages det indtastede ikke, og bruger skal indtaste email igen
def email_check():
    try:
        email_in = input("Please enter Users e-mail: ")
        if "@" and "." in email_in:
            return email_in
        else: 
            raise ValueError
    except ValueError:
        print("please enter a valid e-mail. ")
        email_check()

# initials_check ser efter om de indtastede initialer er mellemn 1 og 4 tegn.
def initials_check():
    try:
        initials_in = str(input("Please enter Users initials  (max 4 characters) "))
        assert initials_in, "Please enter 1 - 4 characters"
        if len(initials_in) > 4:
            raise ValueError
        else: 
            return initials_in
    except AssertionError as error:
        print(error)
        initials_check()
    except TypeError:
        print("please enter initials with letters only. ")
        initials_check()
    except ValueError:
        print("Max 4 characters. ")
        initials_check()

# access_check ser udelukkende efter om der er brugt et passende tal (1-6)
def access_check():
    try:
        access_in = input("Please enter Users Access level  (1-6) ")
        test_access = eval(access_in)
        if not isinstance(int(test_access), int):
            raise TypeError
        elif not len(access_in) == 1:
            raise ValueError
        else: 
            return test_access
    except TypeError:
        print("please enter access level using a number. ")
        access_check()
    except ValueError:
        print("Access level is single digit. ")
        access_check()    

