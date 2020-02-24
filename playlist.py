import song
from extracting_details_mp3 import details_extract as get_song


class Playlist:

    def __init__(self, name, playlist_id, user_id, conn, cursor):
        self.name = name
        self.id = playlist_id
        self.user_id = user_id
        self.conn = conn
        self.cursor = cursor
        self.songs = self.search_for_song_in_db()

    def insert_song_into_db(self, name, artist, length, path):
        song_ = (self.id, self.user_id, name, artist, length, path)
        sql = ("INSERT INTO songs (playlistID, userID, song_name, artist, length, path) VALUES(?, ?, ?, ?, ?, ?)")

        try:
            self.cursor.execute(sql, song_)
            self.conn.commit()
            print("Added song successfully.")

        except NameError as err:
            print(err)

        except Exception as exception:
            print(exception)

    def add_song(self):
        # name = input("Enter song name: ")
        # artist = input("Enter artist: ")
        # length = input("Enter length (format min:sec): ")

        song_ = get_song.open_file_dialog()
        print(song_)
        name = song_['name']
        artist = song_['artist']
        length = song_['length']
        path = song_['path']

        self.songs.append(song.Song(name, artist, length, path))

        self.insert_song_into_db(name, artist, length, path)

    def delete_song(self, index):
        sql = ("DELETE FROM SONGS WHERE song_name = ?")

        try:
            self.cursor.execute(sql, (self.songs[index - 1].name, ))

        except NameError as err:
            print("Something went wrong!")
            print(err)

        else:
            self.conn.commit()
            self.songs.remove(self.songs[index - 1])
            print("Deleted song.")

    def search_for_song_in_db(self):
        sql = ("SELECT song_name, artist, length, path FROM songs WHERE playlistID = ?")
        self.cursor.execute(sql, (self.id,))
        fetched_songs = self.cursor.fetchall()

        if (fetched_songs != None):
            songs = []
            for row in fetched_songs:
                songs.append(song.Song(row[0], row[1], row[2], row[3]))

            return songs

        else:
            return []
