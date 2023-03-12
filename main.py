from tkinter import *
from PIL import ImageTk,Image

root = Tk()
myImg = ImageTk.PhotoImage(Image.open("horse.PNG"))
myLabel = Label(image = myImg)
myLabel.pack()
root.mainloop()