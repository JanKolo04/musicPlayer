from tkinter import *
from tkinter import filedialog
from pygame import mixer
from PIL import ImageTk, Image
from pathlib import Path


root = Tk()
root.title("Music Player")
root.geometry('320x400')
root.resizable(0,0)

#function to load button
def load():
	global plik
	plik = filedialog.askopenfilename()

	path = Path(plik)
	song_name = path.name
	label = Label(root, text=song_name)
	label.pack()


Load = Button(root, text="Load", command=load)
Load.pack()


#function to play button
def play():
	if plik:
		mixer.init()
		mixer.music.load(plik)
		mixer.music.play()

Play = Button(root, text="Play", command=play)
Play.pack()

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


#image
my_pic = Image.open("images/nutka.jpeg")

resized = my_pic.resize((100, 100), Image.ANTIALIAS)

new_pic = ImageTk.PhotoImage(resized)

my_label = Label(root, image=new_pic)
my_label.pack(pady=90)



#button places
Load.place(x=10,y=10);Play.place(x=80,y=350);Pause.place(x=180,y=350);

root.mainloop()