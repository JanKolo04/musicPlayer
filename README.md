# musicPlayer
Music Player

#Music player actualy design

<img width="442" alt="Zrzut ekranu 2021-09-3 o 17 51 21" src="https://user-images.githubusercontent.com/76879087/132033387-097bff4f-3dda-4d0f-8991-ce12574e11fc.png">


#How i want to app look 

![new_design](https://user-images.githubusercontent.com/76879087/132889944-282fc089-626b-4f3a-8b9b-feac06b42594.png)


## Instaling needed libraries
```
pip install tkinter
pip instal pillow
pip install pygame
```


# What we need from following libraries
```
from tkinter import *
from pygame import mixer
from PIL import ImageTk, Image
```


## code of playlist box
```Python
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
	mixer.music.play(loops=0)


Play = Button(root, image=play_pick, borderwidth=0, command=play)
Play.grid()
Play.place(x=160,y=353, height=34, width=48)
```



## TO DO

- [x] make next and previus button
- [x] volume level 
- [x] photo on buttons 
- [ ] the current playing song
def song_data()
https://github.com/srinidhi14vaddy/MP3-Player-using-Tkinter-and-Mutagen-in-Python/blob/master/mp3.py


- [x] duraction and lenght song 
- [ ] delete play button and leave only play/pause
- [ ] add song slider
