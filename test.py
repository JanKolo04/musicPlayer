from tkinter import *
import tkinter.ttk as ttk
from tkmacosx import *


root = Tk()
root.minsize(290, 100)
root.title("My Window")
root.config(background='black')


style = ttk.Style()
style.configure("myStyle.Horizontal.TScale", highlightsbackground="#505050")

scale = ttk.Scale(root, from_=0, to=100, orient=HORIZONTAL, style="myStyle.Horizontal.TScale")
scale.pack()

root.mainloop()

