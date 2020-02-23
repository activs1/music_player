import playlist
import player

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
        pass

    def change_password(self):
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
        playlist_ = playlist.Playlist(name, id, self.id, self.conn, self.cursor)
        self.playlists.append(playlist_)


    def logout(self):
        player_ = player.Player()


