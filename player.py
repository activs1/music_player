import getpass
import sqlite3
import user

class Player:

    def __init__(self):
        self.conn = sqlite3.connect("users_db/users.db")
        self.cursor = self.conn.cursor()
        self.user = None
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
            self.user = user.User(username, password, id, self.conn, self.cursor)
            self.welcome_screen()

        else:
            print("Something went wrong! :(")
            print("Try again.")
            self.login()

    def login_screen(self):
        print("Welcome! What do you want to do?\n")
        choice = input("Login? (press L)\nRegister? (press R)")

        if(choice.upper() == 'L'):
            self.login()

        elif(choice.upper() == 'R'):
            self.registration()

    def welcome_screen(self):
        print("Hello there ", self.user.username, ". Below is a list of options! Choose what you want to do:")

        # Options:
        # 1. Enter playlists
        # 2. Show all songs
        # 3. Change username
        # 4. Change password
        # 5. Logout

        print("--------------------------------")
        print("Enter playlists (press 1)")
        print("Show all songs (press 2)")
        print("Change username (press 3)")
        print("Change password (press 4)")
        print("Logout (press 5)")

        choice = 0
        while choice not in range(1, 5):
            choice = int(input("Your choice: "))

            #Playlists
            if(choice == 1):
                print("Option 1")
                self.playlists_screen()
                break

            #Songs
            elif(choice == 2):
                print("Option 2")
                self.songs_screen()
                break

            #Change username
            elif(choice == 3):
                print("Option 3")
                self.user.change_username()
                break

            #Change password
            elif(choice == 4):
                print("Option 4")
                self.user.change_password()
                break

            #Logout
            elif(choice == 5):
                print("Option 5")
                self.user.logout()
                break




    def playlists_screen(self):
        if(len(self.user.playlists) == 0):
            print("Uh, it's empty here! Add something. Press A to add a playlist or E to exit to welcome screen.")
            choice = input("Your choice: ")
            if(choice.upper() == 'A'):
                user.add_playlist()
                self.playlists_screen()

            elif(choice.upper() == 'E'):
                self.welcome_screen()

        else:
            print("Here are your playlists: ")
            for playlist_ in self.user.playlists:
                print("ID: ", playlist_.id, " | ", playlist_.name)

            print("What next? Choose one of the below options: ")

            # Options:
            # 1. Choose playlist
            # 2. Add playlist
            # 3. Go to welcome screen


            print("--------------------------------")
            print("Choose playlist (press 1)")
            print("Add playlist (press 2)")
            print("Go to welcome screen (press 3)")

            choice = 0
            while choice not in range(1, 5):
                choice = int(input("Your choice: "))

                # Choose playlist
                if (choice == 1):
                    print("Which playlist? Enter below: ")
                    self.songs_screen(int(input()))
                    break

                # Add playlist
                elif (choice == 2):
                    self.user.add_playlist()
                    self.playlists_screen()
                    break

                # Go to welcome screen
                elif (choice == 3):
                    self.welcome_screen()
                    break



    def songs_screen(self, playlist_index):
        print("Playlist name: ", self.user.playlists[playlist_index - 1].name)

        if(len(self.user.playlists[playlist_index - 1].songs) == 0):
            print("Oh, it's empty here. Add a song: ")
            self.user.playlists[playlist_index - 1].add_song()

        else:
            print("NAME   |   ARTIST   |   LENGTH")
            for song in self.user.playlists[playlist_index - 1].songs:
                print(song.name, "   |   ", song.artist, "   |   ", song.length)