from pygame import mixer
import time

loading_char = '#'
percentage_interval = 1  # percent of the song


class Song:

    def __init__(self, name, artist, length, path):
        self.name = name
        self.artist = artist
        self.length = length
        self.path = path

    def play_song(self):
        mixer.quit()
        mixer.pre_init(48000, -16, 1, 1024)
        mixer.init()
        # print(mixer.get_init())
        mixer.music.load(self.path)
        mixer.music.play()

        # mixer.music.stop()

        print("0:00: ", end=' ')

        for i in range(0, int(100 / percentage_interval)):
            print(loading_char, end='')
            time.sleep((float(self.length) * 60) * (percentage_interval / 100))
