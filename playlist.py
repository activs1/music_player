import song

class Playlist:

    def __init__(self, name, playlist_id, user_id, conn, cursor):
        self.name = name
        self.id = playlist_id
        self.user_id = user_id
        self.conn = conn
        self.cursor = cursor
        self.songs = self.search_for_song_in_db()


    def insert_song_into_db(self, name, artist, length):
        song_ = (self.id, self.user_id, name, artist, length)
        sql = ("INSERT INTO songs (playlistID, userID, song_name, artist, length) VALUES(?, ?, ?, ?, ?)")

        try:
            self.cursor.execute(sql, song_)
            self.conn.commit()
        except NameError:
            print(NameError)



    def add_song(self):
        name = input("Enter song name: ")
        artist = input("Enter artist: ")
        length = input("Enter length (format min:sec): ")


        self.songs.append(song.Song(name, artist, length))

        self.insert_song_into_db(name, artist, length)


    def search_for_song_in_db(self):
        sql = ("SELECT song_name, artist, length FROM songs WHERE playlistID = ?")
        self.cursor.execute(sql, (self.id, ))
        fetched_songs = self.cursor.fetchall()

        if (fetched_songs != None):
            songs = []
            for row in fetched_songs:
                songs.append(song.Song(row[0], row[1], row[2]))

            return songs

        else:
            return []