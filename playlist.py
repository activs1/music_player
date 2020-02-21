import song

class Playlist:

    def __init__(self, name, id, cursor, conn):
        self.name = name
        self.id = id
        self.songs = self.search_for_song_in_db()
        self.cursor = cursor
        self.conn = conn
        pass

    def add_song(self, name, artist, length, album = None):
        song_ = song.Song(name, artist, length, album)
        self.songs.append(song_)

    def search_for_song_in_db(self):
        pass
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