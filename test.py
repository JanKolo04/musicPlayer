from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.geometry('320x400')

my_pic = Image.open("images/nutka.jpeg")

resized = my_pic.resize((100, 100), Image.ANTIALIAS)

new_pic = ImageTk.PhotoImage(resized)

my_label = Label(root, image=new_pic)
my_label.pack(pady=80)

root.mainloop()