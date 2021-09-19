# musicPlayer
Music Player

# Music player design

![image](https://user-images.githubusercontent.com/76879087/133936448-e1b35fad-8b72-4d54-b303-abd48b003a7f.png)


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
```



## TO DO

- [x] make next and previus button
- [x] volume level 
- [x] photo on buttons 
- [x] the current playing song
- [x] duraction and lenght song 
- [x] add song slider
- [x] design of current song label



