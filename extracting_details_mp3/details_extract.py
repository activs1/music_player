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









