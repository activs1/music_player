# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 11:57:07 2020

@author: Maciek
"""
from win32com.propsys import propsys, pscon
import tkinter as tk
from tkinter import filedialog
import playsound


def get_music_file_info(path):
    
    '''
    
    Using win32com, this function gets path to a file and 
    based on PKEY values, according to https://docs.microsoft.com/en-us/windows/win32/,
    returns a dictionary of path, name, artist and length [min] of a song
    
    '''
    
    
    try:
        properties = propsys.SHGetPropertyStoreFromParsingName(path)
        
    except Exception as exception:
        print("Something went wrong.")
        print(exception)
        return None
    
    except NameError as err:
        print("Something went wrong.")
        print(err)
        return None
    
    else:
        artist = properties.GetValue(pscon.PKEY_Music_Artist).GetValue()[0]
        name = properties.GetValue(pscon.PKEY_Title).GetValue()
        length = properties.GetValue(pscon.PKEY_Media_Duration).GetValue() #returns duration in 100ns units
        
        length_minutes = length * 100 / (pow(10, 9) * 60)
        #multiplying by 100 to get length in ns unit, then dividing by 10^9 to get seconds
        #and then dividing again by 60 to get minutes
        
        return {
            'path': path,
            'name': name,
            'artist': artist,
            'length': length_minutes
            }
        
    


def open_file_dialog():
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename().replace("/", "\\")


    info = get_music_file_info(file_path)
    return info




##playsound.playsound("C:\\Users\\Maciek\\Desktop\\Rise Against - Savior.mp3".encode('utf-8'), True)
#
#
#from pydub import AudioSegment
#from pydub.playback import play
#
#
#song = AudioSegment.from_mp3(file = 'C:\\Users\\Maciek\\Desktop\\Rise Against - Savior.mp3')
#
##song.export("final.wav", format="wav")
#
#
#
##import simpleaudio as sa
##
##wave_obj = sa.WaveObject.from_wave_file(r"C:\Users\Maciek\Desktop\Rise Against - Savior.mp3")
##play_obj = wave_obj.play()
##play_obj.wait_done()
#
##import vlc
##p = vlc.MediaPlayer("C:/Users/Maciek/Desktop/Rise Against - Savior.mp3")
##p.play()




from pygame import mixer

mixer.init()
mixer.music.load("C:/Users/Maciek/Desktop/Rise Against - Savior.mp3")
mixer.music.stop()
#mixer.music.unload()



















