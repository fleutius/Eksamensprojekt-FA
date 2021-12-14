
# os benyttes i hash funktionen for at give en tilfældig salt. hashlib benyttes til at kryptere password med en sha256 kryptering
import os
import hashlib

class User:    
    def __init__(self,initials ,first_name, last_name, email, access_level):
        self.initials = initials
        self.first_name = first_name
        self.last_name = last_name
        self.name = (first_name + ' ' + last_name)
        self.email = email
        self.access_level = access_level
        self.salt = os.urandom(32)
        # Brugeren indtaster password så snart en User instance laves. 
        self.password = input("Please choose your password: ")
        # Herefter hashes det indtastede password med sha256 kryptering samt med en ekstra "salt" del, som gør det væsentligt mere besværligt at brute force passworded, selv hvis systemet skulle blive udsat for et datalæk,
        # da det kun vil være muligt at finde frem til hash værdien af passworded sammen med salt key
        self.key = hashlib.pbkdf2_hmac(
            'sha256',
            self.password.encode('utf8'),
            self.salt,
            100000,
            dklen=128
        )
        # Så snart passworded er blevet hashed, gemmes kombinationen af salt og key, i en variabel til senere at kunne verificere brugeren, når passworded indtastes. 
        self.storedpass = self.salt + self.key
        # Direkte herefter slettes variablen med brugerens indtastede password. Passworded gemmes hermed ingen steder i systemet, og vil på intet tidspunkt være tilgængeligt i den rå form, da krypteringen sker automatisk.
        self.password = ''
        
        self.user_file = open("user_file.txt", "a")

    # user_registration ser om de 2 af de indtastede variabler som skal være unikke, er tilstede i user_file.txt. Hvis dette ikke er tilfældet, skrives data til filen. Hvis funktionen finder data dublikation, informeres brugeren, og skal indtaste en anden data.
    def user_registration(self):
        with open("user_file.txt", "a+") as check_file:
            try:
                assert self.initials not in check_file.read(), "Initials is allready registrered"
                assert self.email not in check_file.read(), "Email is allready registrered"
            except AssertionError as error:
                print(error)
            else: 
                lines = f"{self.initials} - {self.name} - {self.email} - {self.access_level} - {self.key}\n" 
                self.user_file.writelines(lines)
                print("The requested user has been registered ")
            finally: check_file.close()

    def file_read():
        with open("user_file.txt", 'r') as f:
            read_file = f.readlines()
            for line in read_file:
                wordInLine = line.split("-")
                print(f"Initialer: {wordInLine[0]}\nNavn: {wordInLine[1]}\nEmail: {wordInLine[2]}\nprofil: {wordInLine[3]}\nHashed Kode: {wordInLine[4]}")

    # empty_file er ikke tilgængelig for brugeren, men kan benyttes af f.eks. administrator, til nemt og effiktivt at slette alt indhold af user_file.txt
    def empty_file():
        open("user_file.txt", 'w')

    def print_user(self):
        print("Full Name: ")
        print(self.name)
        print("Email: ")
        print(self.email)

    def view_access(self):
        print(f"User: {self.initials} has acces level {self.access_level}")



