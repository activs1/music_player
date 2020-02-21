import playlist
import player

class User:

    def __init__(self, username, password, id, conn, cursor):
        self.username = username
        self.password = password
        self.conn = conn
        self.cursor = cursor
        self.id = id
        self.playlists = self.search_for_playlists_in_db()
        self.welcome_screen()

    def welcome_screen(self):
        print("Hello there ", self.username, ". Below is a list of options! Choose what you want to do:")

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
                self.change_username()
                break

            #Change password
            elif(choice == 4):
                print("Option 4")
                self.change_password()
                break

            #Logout
            elif(choice == 5):
                print("Option 5")
                self.logout()
                break


    def search_for_playlists_in_db(self):
        sql = ("SELECT playlist_name, playlistID FROM playlists WHERE userID = ?")
        self.cursor.execute(sql, (self.id, ))

        fetched_playlists = self.cursor.fetchall()
        if(fetched_playlists != None):
            playlists = []
            for row in fetched_playlists:
                playlists.append(playlist.Playlist(row[0], row[1]))

            return playlists

        else:
            return []



    def change_username(self):
        pass

    def change_password(self):
        pass

    def playlists_screen(self):
        if(len(self.playlists) == 0):
            print("Uh, it's empty here! Add something. Press A to add a playlist or E to exit to welcome screen.")
            choice = input("Your choice: ")
            if(choice.upper() == 'A'):
                self.add_playlist()
                self.playlists_screen()

            elif(choice.upper() == 'E'):
                self.welcome_screen()

        else:
            print("Here are your playlists: ")
            for playlist_ in self.playlists:
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
                    self.add_playlist()
                    self.playlists_screen()
                    break

                # Go to welcome screen
                elif (choice == 3):
                    self.welcome_screen()
                    break


    def songs_screen(self, playlist_index):
        print("Playlist name: ", self.playlists[playlist_index].name)
        for song in self.playlists[playlist_index].songs:
            pass


    def insert_playlist_into_db(self, name):
        """
        This method inserts a playlist into table playlists in users.db

        name --> name of the playlist

        If successful returns ID of the created playlist (playlistID is a autoincrement column in playlists table)
        If not successful prints raised Error and return a None type object

        """

        playlist_ = (name, self.id)
        sql = ("INSERT INTO playlists (playlist_name, userID) VALUES (?, ?)")
        try:
            self.cursor.execute(sql, playlist_)
            id = self.cursor.lastrowid
            self.conn.commit()
            return id
        except NameError:
            print(NameError)
            return None


    def add_playlist(self):
        print("So you want to add playlist. Ok, follow instructions below.")
        name = input("Enter playlist name: ")

        id = self.insert_playlist_into_db(name)
        playlist_ = playlist.Playlist(name, id)
        self.playlists.append(playlist_)


    def logout(self):
        player_ = player.Player()


