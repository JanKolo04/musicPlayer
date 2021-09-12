<<<<<<< HEAD
from tkinter import * 
import tkinter.ttk as ttk
from tkmacosx import *

root = Tk()
root.geometry('290x100')
root.config(background='black')

=======
from tkinter import *
import tkinter.ttk as ttk


root = Tk()
root.minsize(290, 100)
root.title("My Window")
root.config(background='black')


>>>>>>> b3d6629b911ddeb84cce8cd7cacf8f77a92a455e
scale = ttk.Scale(root, from_=0, to=100, length=100, orient=HORIZONTAL)
scale.pack()

style = ttk.Style()
style.configure('Horizontal.TScale', bd=0, background='black')
<<<<<<< HEAD
=======
style.map('Horizontal.TScale', )
>>>>>>> b3d6629b911ddeb84cce8cd7cacf8f77a92a455e

root.mainloop()