from tkinter import *
from tkinter import Label
from tkinter import filedialog
from pygame import mixer
from PIL import ImageTk, Image

class MusicPlayer:
    def __init__(self, window):
        global Pause, toggleText
        window.geometry('320x400'); window.title('Iris Player'); window.resizable(0,0)
        Load = Button(window, text = 'Load',  width = 10, font = ('Times', 10), command = self.load)
        Play = Button(window, text = 'Play',  width = 10,font = ('Times', 10), command = self.play)
        Pause = Button(window, text = 'Pause',  width = 10,font = ('Times', 10), command = self.pause)
        Load.place(x=10,y=10);Play.place(x=80,y=350);Pause.place(x=180,y=350);
        self.music_file = False
        self.playing_state = False 
        self.toggleText = False
    
    def Photo():
        photo = PhotoImage('okej.png')

        label = Label(image=photo)
        label.image = photo # keep a reference!
        label.pack()

    def toggleText(self):
      if (Pause['text'] == 'Pause'):
        Pause['text'] = 'Unpause'
      else:
        Pause['text'] = 'Pause'

    def load(self):
        self.music_file = filedialog.askopenfilename()

    def play(self):
        if self.music_file:
            mixer.init()
            mixer.music.load(self.music_file)
            mixer.music.play()

    def pause(self):
        self.toggleText = toggleText(self)
        Pause = Button(command = self.toggleText)
        if not self.playing_state:
            mixer.music.pause()
            self.playing_state=True
        else:
            mixer.music.unpause()
            self.playing_state = False




root = Tk()
app= MusicPlayer(root)
root.mainloop()
