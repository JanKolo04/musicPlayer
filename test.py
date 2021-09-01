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


frame = LabelFrame(root, text='Volume')
frame.grid(row=5, column=0, padx=50, pady=300)


scale = Scale(frame, from_=0, to=100, orient=HORIZONTAL, command=volume)
scale.set(50)
scale.pack()



root.mainloop()