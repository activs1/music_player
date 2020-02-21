import getpass
import sqlite3
import user

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


    def check_user(self, username, password):
        user_ = (username, password)
        sql = ("SELECT username, password, ID FROM users_data WHERE username = ? AND password = ?")
        self.cursor.execute(sql, user_)
        fetched_row = self.cursor.fetchone()

        if(fetched_row != None and (fetched_row[0] == username and fetched_row[1] == password)):
            return True, fetched_row[2]
        else:
            return False, None

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
        user_ok, id = self.check_user(username, password)
        if (user_ok):
            print("Logged in successfully! :)")
            user_ = user.User(username, password, id, self.conn, self.cursor)

        else:
            print("Something went wrong! :(")

    def login_screen(self):
        print("Welcome! What do you want to do?\n")
        choice = input("Login? (press L)\nRegister? (press R)")

        if(choice.upper() == 'L'):
            self.login()

        elif(choice.upper() == 'R'):
            self.registration()