from tkinter import *
from tkinter import filedialog
from pygame import mixer


root = Tk()
root.geometry('320x400')
root.resizable(0,0)

def load():
	filedialog.askopenfilename()

button = Button(root, text="Load", command=load)
button.pack()


root.mainloop()