import getpass
import sqlite3

class Player:

    def __init__(self):
        self.conn = sqlite3.connect("users_db/users.db")
        self.cursor = self.conn.cursor()
        self.login_screen()

    def insert_user_into_db(self, username, password):
        user = (username, password)
        sql = ("INSERT INTO users_data (username, password) VALUES (?, ?)")
        self.cursor.execute(sql, user)
        self.conn.commit()

    #unused function, SQL manages data now
    def create_unique_file(self, username, password):
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

    def check_user(self, username, password):
        user = (username, password)
        sql = ("SELECT username, password FROM users_data WHERE username = ? AND password = ?")
        self.cursor.execute(sql, user)
        fetched_row = self.cursor.fetchone()
        print(fetched_row)
        if(fetched_row[0] == username and fetched_row[1] == password):
            return True
        else:
            return False

    def registration(self):
        print("Hello first time user!\nEnter your username and password below so we can add them to our database!")
        username = input("Enter username: ")
        password = getpass.getpass("Enter password: ")

        #
        #self.create_unique_file(username, password)
        #

        self.insert_user_into_db(username, password)

    def login(self):
        print("Hello!\nEnter your username and password below to login.")

        username = input("Enter username: ")
        password = getpass.getpass("Enter password: ")
        if (self.check_user(username, password)):
            print("Logged in successfully! :)")

        else:
            print("Something went wrong! :(")

    def login_screen(self):
        print("Welcome! What do you want to do?\n")
        choice = input("Login? (press L)\nRegister? (press R)")

        if(choice.upper() == 'L'):
            self.login()

        elif(choice.upper() == 'R'):
            self.registration()