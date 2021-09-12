from tkinter import *
import tkinter.ttk as ttk


root = Tk()
root.minsize(290, 100)
root.title("My Window")
root.config(background='black')


style = ttk.Style()
style.configure("myStyle.Horizontal.TScale", background="#505050")

scale = ttk.Scale(root, from_=0, to=100, orient=HORIZONTAL, style="myStyle.Horizontal.TScale")
scale.pack()

root.mainloop()
<<<<<<< HEAD
=======

>>>>>>> 4f101c7994d2e7c10ccfd317d8b12fc93e81813d
