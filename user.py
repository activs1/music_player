import playlist
import player
import getpass

class User:

    def __init__(self, username, password, user_id, conn, cursor):
        self.username = username
        self.password = password
        self.conn = conn
        self.cursor = cursor
        self.id = user_id
        self.playlists = self.search_for_playlists_in_db()

    def search_for_playlists_in_db(self):
        sql = ("SELECT playlist_name, playlistID FROM playlists WHERE userID = ?")
        self.cursor.execute(sql, (self.id, ))

        fetched_playlists = self.cursor.fetchall()
        if(fetched_playlists != None):
            playlists = []
            for row in fetched_playlists:
                playlists.append(playlist.Playlist(row[0], row[1], self.id, self.conn, self.cursor))

            return playlists

        else:
            return []



    def change_username(self):
        new_username = input("Enter new username: ")

        if(input("Confirm password: ") == self.password):
            print("Changing username...")

            user_ = (new_username, self.id)
            sql = ("UPDATE users_data SET username = ? WHERE ID = ?")

            try:
                self.cursor.execute(sql, user_)
                self.conn.commit()
                self.username = new_username
                print("Changed username!")

            except NameError:
                print("Something went wrong: ")
                print(NameError)

        else:
            print("Wrong password! Try again.")
            self.change_username()

    def change_password(self):
        new_password = getpass.getpass("Enter new password: ")

        if (input("Enter previous password: ") == self.password):
            print("Changing password...")

            user_ = (new_password, self.id)
            sql = ("UPDATE users_data SET password = ? WHERE ID = ?")

            try:
                self.cursor.execute(sql, user_)
                self.conn.commit()
                self.password = new_password
                print("Changed password!")

            except NameError:
                print("Something went wrong: ")
                print(NameError)

        else:
            print("Wrong password! Try again.")
            self.change_username()



    def insert_playlist_into_db(self, name):
        """
        This method inserts a playlist into table playlists in users.db

        name --> name of the playlist

        If successful returns ID of the created playlist (playlistID is a autoincrement column in playlists table)
        If not successful prints raised Error and returns a None type object

        """

        playlist_ = (name, self.id)
        sql = ("INSERT INTO playlists (playlist_name, userID) VALUES (?, ?)")
        try:
            self.cursor.execute(sql, playlist_)
            id = self.cursor.lastrowid
            self.conn.commit()
            return id

        except Exception as exception:
            print(exception)
            return None

        except NameError as err:
            print(err)
            return None


    def add_playlist(self):
        print("So you want to add playlist. Ok, follow instructions below.")
        name = input("Enter playlist name: ")

        id = self.insert_playlist_into_db(name)
        playlist_ = playlist.Playlist(name, id, self.id, self.conn, self.cursor)
        self.playlists.append(playlist_)

    def delete_playlist(self, playlist_id, index):
        sql = ("DELETE FROM playlists WHERE playlistID = ?")

        try:
            self.cursor.execute(sql, (playlist_id, ))

        except NameError:
            print("Something went wrong.")
            print(NameError)

        else:
            self.conn.commit()
            self.playlists.remove(self.playlists[index - 1])
            print("Deleted playlist.")


    def logout(self):
        del self
        player_ = player.Player()


