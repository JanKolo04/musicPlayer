from tkinter import *
from tkinter import filedialog
from pygame import mixer
from PIL import ImageTk, Image
from pathlib import Path
import os

root = Tk()
root.title("Music Player")
root.geometry('800x400')

def volume(val):
	volume = int(val) / 100
	mixer.init()
	mixer.music.set_volume(volume)


scale = Scale(root, from_=0, to=100, orient=HORIZONTAL, command=volume)
scale.set(50)
scale.pack()

root.mainloop()