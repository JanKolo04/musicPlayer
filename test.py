'''root = Tk()
root.geometry('400x200')
root.resizable(0,0)
root.title("My Window")
root.config(background='white')


make a three label 

--------------------
	   Sldier
--------------------
0:00     |      3:28
---------|----------

One for slider and nexts two for music time
left time set posittion on anchor=W
right time set posittion on anchor=E
and make slider with margin:20px;



my_slider = ttk.Scale(root, from_=0, to=100, orient=HORIZONTAL, value=0, length=360)
my_slider.grid()
my_slider.place(x=20, y=120, height=30)


Time1_label = Label(root, text='Time1', bg='black', fg='white', anchor=W)
Time1_label.grid()
Time1_label.place(y=150, width=200, height=50)

Time2_label = Label(root, text='Time2', bg='green', anchor=E)
Time2_label.grid()
Time2_label.place(y=150, x=200, width=200, height=50)


root.mainloop()'''

'''

92 Explorer
Post Malone 


1.Label
#in next button
2.label.config(next_song)
#in previous song
3.label.config(previous_song)




'''




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


#photo on previous button
previous_image = Image.open('images/previous.png')

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

'''#exit button
exit = Button(root, text='Exit',  image=exit_pick, bd=0,command=root.destroy)
exit.grid()
exit.place(x=380, y=10, height=40, width=40)

'''

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




	#text
	#Text = f'   {converted_current_time} 		 		           	         {converted_song_lenght}'
	#Output time in text bar
	#status_bar.config(text=Text)

	#update slider posittion to current song posittion
	#my_slider.config(value=current_time)


	#update time
	status_bar1.after(1000, play_time)
	status_bar2.after(1000, play_time)



#volume
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
scale.pack()



#bottom belt
down_belt = Label(root, bg='#424242')
down_belt.grid()
down_belt.place(x=0, y=440, height=60, width=440)



#function to play button
songsframe = LabelFrame(root,text="Song Playlist",font=("times new roman",15,"bold"),bg="grey",fg="white",bd=5,relief=GROOVE)
songsframe.place(x=20, y=1,width=400,height=200)
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
Play.place(x=160,y=453, height=34, width=48)

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
Pause.place(x=240,y=453, height=34, width=48)


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



def slide(x):
	mixer.music.load(playlist.get(ACTIVE))
	mixer.music.play(loops=0, start=int(my_slider.get()))



Previous = Button(root, image=previous_pick, borderwidth=0, command=previous_button)
Previous.grid()
Previous.place(x=80,y=450, height=40, width=40)


status_bar1 = Label(root, text='', bg='black', fg='white', bd=1, anchor=W)
status_bar1.grid()
status_bar1.place(height=30, width=220, y=410)

status_bar2 = Label(root, text='', bg='black', fg='white', bd=1, anchor=E)
status_bar2.grid()
status_bar2.place(height=30, width=220, x=220, y=410)


#slider
my_slider = ttk.Scale(root, from_=0, to=100, orient=HORIZONTAL, value=0, command=slide, length=360)
my_slider.grid()
my_slider.place(x=40, y=390, height=20)

#current song
current_song = Label(root, text='', bg='black', fg='white')
current_song.grid()
current_song.place(y=300,width=440, height=50)

root.mainloop()
