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
root.config(background='black')

#function to load button
'''
def load():
	global plik
	plik = filedialog.askopenfilename()

	path = Path(plik)
	song_name = path.name
	label = Label(root, text=song_name)
	label.pack()


Load = Button(root, text="Load", command=load)
Load.pack()
Load.place(x=10,y=10);
'''

#bottom belt
down_belt = Label(root, bg='#424242')
down_belt.pack()
down_belt.place(x=0, y=360, height=40, width=440)

#function to play button
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
Play.pack()
Play.place(x=140,y=370, width=57);

#function to pause button
def toggleText():
	if (Pause['text'] == 'Pause'):
		Pause['text'] = 'Unpause'
	else:
		Pause['text'] = 'Pause'


playing_state = False 
def pause():
	global playing_state

	if not playing_state:
		mixer.music.pause()
		playing_state = True
	else:
		mixer.music.unpause()
		playing_state = False


Pause = Button(root, text="Pause", command=lambda:[toggleText(), pause()])
Pause.pack()
Pause.place(x=240,y=370, width=57);




root.mainloop()



