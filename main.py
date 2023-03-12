from tkinter import *
from PIL import ImageTK,Image

root = Tk()
myImg = ImageTK.PhotoImage(Image.open("horse.PNG"))
myImg.pack()
root.mainloop()