from tkinter import * 
import tkinter.ttk as ttk
from tkmacosx import *

root = Tk()
root.geometry('290x100')
root.config(background='black')

scale = ttk.Scale(root, from_=0, to=100, length=100, orient=HORIZONTAL)
scale.pack()

style = ttk.Style()
style.configure('Horizontal.TScale', bd=0, background='black')

root.mainloop()