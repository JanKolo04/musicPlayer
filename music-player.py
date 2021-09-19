from tkinter import *
from tkinter import filedialog
from pygame import mixer
from PIL import ImageTk, Image
from pathlib import Path
import os
import time
from mutagen.mp3 import MP3
import tkinter.ttk as ttk

root = Tk()
root.title("Music Player")
root.geometry('440x500')
root.resizable(0,0)
root.config(background='black')

'''
IMAGES
'''

#photo on play button
play_image = Image.open('images/play3.png')

resized_play = play_image.resize((40,40), Image.ANTIALIAS)

play_pick = ImageTk.PhotoImage(resized_play)


#photo on pause button
pause_image = Image.open('images/pause3.png')

resized_pause = pause_image.resize((40,40), Image.ANTIALIAS)

pause_pick = ImageTk.PhotoImage(resized_pause)


#photo on next button
next_image = Image.open('images/next3.png')

resized_next = next_image.resize((40,40), Image.ANTIALIAS)

next_pick = ImageTk.PhotoImage(resized_next)


#photo on previous button
previous_image = Image.open('images/previous3.png')

resized_previous = previous_image.resize((40,40), Image.ANTIALIAS)

previous_pick = ImageTk.PhotoImage(resized_previous)



#button on previou button
exit_image = Image.open('images/exit.png')

resized_exit = exit_image.resize((45,40), Image.ANTIALIAS)

exit_pick = ImageTk.PhotoImage(resized_exit)


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

#exit button
exit = Button(root, text='Exit',  image=exit_pick, bd=0,command=root.destroy)
exit.grid()
exit.place(x=390, y=10, height=40, width=40)



#grab song lenght time info
def play_time():
	global song_lenght
	#grab current song elapsed time
	current_time = mixer.music.get_pos() / 1000

	#convert to time format
	converted_current_time = time.strftime('%M:%S', time.gmtime(current_time))

	#mutagen
	current_song = playlist.curselection()
	song = playlist.get(current_song)

	song_mut = MP3(song)
	song_lenght = song_mut.info.length
	converted_song_lenght = time.strftime('%M:%S', time.gmtime(song_lenght))



	#current time by 1 second
	current_time += 1

	if int(my_slider.get()) == int(song_lenght):
		#text
		Text = f'{converted_song_lenght}'
		#Output time in text bar
		status_bar2.config(text=Text)
	elif playing_state:
		pass

	elif int(my_slider.get()) == int(current_time):
		#slider hasnt been moved
		#update slide posittion
		slider_posittion = int(song_lenght)
		my_slider.config(to=slider_posittion, value=int(current_time))
	else:
		#slider has been moved
		#update slide posittion 
		slider_posittion = int(song_lenght)
		my_slider.config(to=slider_posittion, value=int(my_slider.get()))
		
		#convert to time format
		converted_current_time = time.strftime('%M:%S', time.gmtime(int(my_slider.get())))

		#text
		Text1 = f'{converted_current_time}'
		#Output time in text bar
		status_bar1.config(text=Text1)

		Text2 = f'{converted_song_lenght}'
		status_bar2.config(text=Text2)

		#move this thing along by one seckond 
		next_time = int(my_slider.get()) + 1
		my_slider.config(value=next_time)


	#update time
	status_bar1.after(1000, play_time)
	status_bar2.after(1000, play_time)



'''#volume
def volume(val):
	volume = int(val) / 100
	mixer.init()
	mixer.music.set_volume(volume)

#volume frame
frame = LabelFrame(root, text='Volume', cursor='arrow')
frame.grid(row=5, column=0, padx=165, pady=220)

#volume slider
scale = Scale(frame, from_=0, to=100, orient=HORIZONTAL, command=volume, length=100)
scale.set(50)
scale.pack()'''


#bottom belt
down_belt = Label(root, bg='black')
down_belt.grid()
down_belt.place(x=0, y=440, height=60, width=440)

#line
line = Canvas(root,width=440, height=3, background='white')
line.grid()
line.place(y=432)



#function to play button
songsframe = LabelFrame(root,text="Song Playlist",font=("times new roman",15,"bold"),bg="grey",fg="white",bd=5,relief=GROOVE)
songsframe.place(x=10, y=80, width=420, height=200)
scrol_y = Scrollbar(songsframe,orient=VERTICAL)
playlist = Listbox(songsframe,yscrollcommand=scrol_y.set,selectbackground="gold",selectmode=SINGLE,font=("times new roman",12,"bold"),bg="grey",fg="navyblue",bd=5,relief=GROOVE)
scrol_y.pack(side=RIGHT,fill=Y)
scrol_y.config(command=playlist.yview)
playlist.pack(fill=BOTH)
os.chdir("songs")
songtracks = os.listdir()
actual_song = 0


#print songs
for track in songtracks:
	playlist.insert(END,track)


def play():
	mixer.init()
	mixer.music.load(playlist.get(ACTIVE))
	mixer.music.play(loops=0)

	play_time()

	#current song
	current_song.config(text=playlist.get(ACTIVE))

	#update sliser posittion
	#slider_posittion = int(song_lenght)
	#my_slider.config(to=slider_posittion, value=0)


Play = Button(root, image=play_pick, borderwidth=0, command=play)
Play.grid()
Play.place(x=160,y=450, height=40, width=40)

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
Pause.place(x=240,y=450, height=40, width=40)


def next_button():
	#reser slider and status bar
	status_bar1.config(text='')
	my_slider.config(value=0)

	status_bar2.config(text='')
	my_slider.config(value=0)

	next_song = playlist.curselection()
	next_song = next_song[0]+1
	song = playlist.get(next_song)

	#current song
	current_song.config(text=song)

	mixer.init()
	mixer.music.load(song)
	mixer.music.play(loops=0)

	playlist.selection_clear(0, END)
	playlist.activate(next_song)
	playlist.selection_set(next_song, last=None)



Next = Button(root, image=next_pick, borderwidth=0, command=next_button)
Next.grid()
Next.place(x=320,y=450, height=40, width=40)



def previous_button():
	#reset slider nad status bar
	status_bar1.config(text='')
	my_slider.config(value=0)

	status_bar2.config(text='')
	my_slider.config(value=0)

	previous_song = playlist.curselection()
	previous_song = previous_song[0]-1
	song = playlist.get(previous_song)

	mixer.init()
	mixer.music.load(song)
	mixer.music.play(loops=0)

	#current song
	current_song.config(text=song)

	playlist.selection_clear(0, END)
	playlist.activate(previous_song)
	playlist.selection_set(previous_song, last=None)


Previous = Button(root, image=previous_pick, borderwidth=0, command=previous_button)
Previous.grid()
Previous.place(x=80,y=450, height=40, width=40)



def slide(x):
	mixer.music.load(playlist.get(ACTIVE))
	mixer.music.play(loops=0, start=int(my_slider.get()))



status_bar1 = Label(root, text='', bg='black', fg='white', bd=1, anchor=W)
status_bar1.grid()
status_bar1.place(height=30, width=220, y=410)

status_bar2 = Label(root, text='', bg='black', fg='white', bd=1, anchor=E)
status_bar2.grid()
status_bar2.place(height=30, width=220, x=220, y=410)


#slider
my_slider = ttk.Scale(root, from_=0, to=100, orient=HORIZONTAL, value=0, command=slide, length=400)
my_slider.grid()
my_slider.place(x=20, y=380, height=20)

#current song
current_song = Label(root, text='', bg='black', fg='white')
current_song.grid()
current_song.place(y=350, width=440, height=20)

root.mainloop()




