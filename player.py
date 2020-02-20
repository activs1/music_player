import getpass
import glob, os


def create_unique_file(username, password):
    fname = open(r"users_db/" + str(username) + ".txt", "w+")
    try:
        fname.write(username)
        fname.write("\n")
        fname.write(password)
    except NameError:
        print("Error occured!", NameError)
    else:
        print("User created successfully!")

    fname.close()


def check_user(username, password):
    os.chdir(r"users_db")

    for file in glob.glob("*.txt"):
        if (file == str(username) + ".txt"):
            fname = open(file, "r")
            lines = fname.readlines()
            if (lines[0] == str(username) + "\n" and lines[1] == str(password)):
                return True
            else:
                return False


def registration():
    print("Hello first time user!\nEnter your username and password below so we can add them to our database!")
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")
    create_unique_file(username, password)


def login():
    print("Hello!\nEnter your username and password below to login.")

    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")
    if(check_user(username, password)):
        print("Logged in successfully! :)")

    else:
        print("Something went wrong! :(")



class Player:

    def __init__(self):
        self.login_screen()

    def login_screen(self):
        print("Welcome! What do you want to do?\n")
        choice = input("Login? (press L)\nRegister? (press R)")

        if(choice.upper() == 'L'):
            login()

        elif(choice.upper() == 'R'):
            registration()