from tkinter import *
from tkinter import filedialog
from pygame import mixer
from PIL import ImageTk, Image
from pathlib import Path
import os


root = Tk()
root.title("Music Player")
root.geometry('440x400')
root.resizable(0,0)


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


def play():
    mixer.init()
    mixer.music.load(playlist.get(ACTIVE))
    mixer.music.play()


Play = Button(root, text="Play", command=play)
Play.grid()
Play.place(x=160,y=368, width=57)



def get_next_song():
    if track + 2 <= len(songtracks):
        return track + 1
    else:
        return 0

def next_song():
    track = get_next_song()
    mixer.init()
    mixer.music.play(track)


Next = Button(root, text="Next", command=next_song)
Next.grid()


root.mainloop()