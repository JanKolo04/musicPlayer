from tkinter import *


root = Tk()
root.geometry('320x400')
root.resizable(0,0)

def toggleText():
	if (Pause['text'] == 'Pause'):
		Pause['text'] = 'Unpause'
	else:
		Pause['text'] = 'Pause'

Pause = Button(root, text="Pause", command=toggleText)
Pause.pack()

root.mainloop()