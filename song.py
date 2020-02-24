import playsound
import time
from pygame import mixer


class Song:

    def __init__(self, name, artist, length, path):
        self.name = name
        self.artist = artist
        self.length = length
        self.path = path


    def play_song(self):
        mixer.init()
        mixer.music.load(self.path)
        mixer.music.play()
        #time.sleep(60 * self.length)




