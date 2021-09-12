from tkinter import *
import tkinter.ttk as ttk


root = Tk()
root.minsize(290, 100)
root.title("My Window")
root.config(background='black')


scale = ttk.Scale(root, from_=0, to=100, length=100, orient=HORIZONTAL)
scale.pack()

style = ttk.Style()
style.configure('Horizontal.TScale', bd=0, background='black')
style.map('Horizontal.TScale', )

root.mainloop()