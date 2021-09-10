from tkinter import *
from tkinter import filedialog
from pygame import mixer
from PIL import ImageTk, Image
from pathlib import Path
import os


root = Tk()
root.title("Music Player")
root.geometry('440x450')
root.resizable(0,0)
root.config(background='black')

'''
IMAGES
'''

#photo on play button
play_image = Image.open('images/play.png')

resized_play = play_image.resize((70,40), Image.ANTIALIAS)

play_pick = ImageTk.PhotoImage(resized_play)


#photo on pause button
pause_image = Image.open('images/pause.png')

resized_pause = pause_image.resize((60,45), Image.ANTIALIAS)

pause_pick = ImageTk.PhotoImage(resized_pause)


#photo on next button
next_image = Image.open('images/next.png')

resized_next = next_image.resize((40,45), Image.ANTIALIAS)

next_pick = ImageTk.PhotoImage(resized_next)


#button on previous button
previous_image = Image.open('images/previous.png')

resized_previous = previous_image.resize((40,40), Image.ANTIALIAS)

previous_pick = ImageTk.PhotoImage(resized_previous)


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

#volume

#edits: add frame to volme slider
def volume(val):
	volume = int(val) / 100
	mixer.init()
	mixer.music.set_volume(volume)


frame = LabelFrame(root, text='Volume', cursor='target')
frame.grid(row=5, column=0, padx=165, pady=250)


scale = Scale(frame, from_=0, to=100, orient=HORIZONTAL, command=volume, length=100)
scale.set(50)
scale.pack()



#bottom belt
down_belt = Label(root, bg='#424242')
down_belt.grid()
down_belt.place(x=0, y=390, height=60, width=440)



#function to play button
songsframe = LabelFrame(root,text="Song Playlist",font=("times new roman",15,"bold"),bg="grey",fg="white",bd=5,relief=GROOVE)
songsframe.place(x=20, y=20,width=400,height=200)
scrol_y = Scrollbar(songsframe,orient=VERTICAL)
playlist = Listbox(songsframe,yscrollcommand=scrol_y.set,selectbackground="gold",selectmode=SINGLE,font=("times new roman",12,"bold"),bg="grey",fg="navyblue",bd=5,relief=GROOVE)
scrol_y.pack(side=RIGHT,fill=Y)
scrol_y.config(command=playlist.yview)
playlist.pack(fill=BOTH)
os.chdir("songs")
songtracks = os.listdir()
actual_song = 0



for track in songtracks:
	playlist.insert(END,track)


def play():
	mixer.init()
	mixer.music.load(playlist.get(ACTIVE))
	mixer.music.play(loops=0)


Play = Button(root, image=play_pick, borderwidth=0, command=play)
Play.grid()
Play.place(x=160,y=403, height=34, width=48)

#function to pause button
playing_state = False 
def pause():
	global playing_state

	if not playing_state:
		mixer.music.pause()
		playing_state = True
	else:
		mixer.music.unpause()
		playing_state = False


Pause = Button(root, image=pause_pick, borderwidth=0, command=pause)
Pause.grid()
Pause.place(x=240,y=403, height=34, width=48)


def next_button():
	next_song = playlist.curselection()
	next_song = next_song[0]+1
	song = playlist.get(next_song)

	mixer.init()
	mixer.music.load(song)
	mixer.music.play(loops=0)

	playlist.selection_clear(0, END)
	playlist.activate(next_song)
	playlist.selection_set(next_song, last=None)



Next = Button(root, image=next_pick, borderwidth=0, command=next_button)
Next.grid()
Next.place(x=320,y=400, height=40, width=40)



def previous_button():
	previosu_song = playlist.curselection()
	previosu_song = previosu_song[0]-1
	song = playlist.get(previosu_song)

	mixer.init()
	mixer.music.load(song)
	mixer.music.play(loops=0)

	playlist.selection_clear(0, END)
	playlist.activate(previosu_song)
	playlist.selection_set(previosu_song, last=None)



Previous = Button(root, image=previous_pick, borderwidth=0, command=previous_button)
Previous.grid()
Previous.place(x=80,y=400, height=40, width=40)




root.mainloop()



