from tkinter import *
from tkinter import filedialog
from pygame import mixer
from PIL import ImageTk, Image
from pathlib import Path
import os

root = Tk()
root.title("MSC")
root.geometry('400x400')

mixer.init()

mxstate = 0

songsframe = LabelFrame(root,text="Song Playlist",font=("times new roman",15,"bold"),bg="grey",fg="white",bd=5,relief=GROOVE)
songsframe.place(x=20, y=20,width=400,height=200)
scrol_y = Scrollbar(songsframe,orient=VERTICAL)
playlist = Listbox(songsframe,yscrollcommand=scrol_y.set,selectbackground="gold",selectmode=SINGLE,font=("times new roman",12,"bold"),bg="silver",fg="navyblue",bd=5,relief=GROOVE)
scrol_y.pack(side=RIGHT,fill=Y)
scrol_y.config(command=playlist.yview)
playlist.pack(fill=BOTH)
os.chdir("songs")
songtracks = os.listdir()

for track in songtracks:
    playlist.insert(END,track)

def play_stop():
    global mxstate

    if mxstate == 0: 
        mixer.music.load(playlist.get(ACTIVE))
        mixer.music.play()
        Play_stop.configure(text = "Pause")
        mxstate =  1
        return

    if mxstate == 1:
        mixer.music.pause()
        Play_stop.configure(text = "Resume")
    else: 
        mixer.music.unpause()
        Play_stop.configure(text = "Pause")
    mxstate = 3-mxstate 
     
Play_stop =Button(root, text='Play', width=14, bg='red', fg='black', command=play_stop)
Play_stop.pack()
Play_stop.place(x=240,y=350, height=40, width=40)


root.mainloop()