from tkinter import *
from tkinter import filedialog
from pygame import mixer
from PIL import ImageTk, Image
from pathlib import Path
import os
from PIL import ImageTk, Image


root = Tk()
root.title("Music Player")
root.geometry('440x400')
root.resizable(0,0)

play_image = Image.open('images/play.png')

resized = play_image.resize((40,40), Image.ANTIALIAS)

play_pick = ImageTk.PhotoImage(resized)


Play = Button(root, image=play_pick)
Play.pack()

root.mainloop()