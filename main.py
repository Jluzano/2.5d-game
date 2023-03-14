from tkinter import *
from PIL import ImageTk,Image
import json

def left(event):
    ImageTk.PhotoImage(Image.open(map["(0, 0)"]["left"]))

m = open("map.json")
map = json.load(m)
root = Tk()
myImg = ImageTk.PhotoImage(Image.open(map["(0, 0)"]["north"]["IMG"]))
myLabel = Label(image = myImg)
myLabel.pack()
root.bind("<Left>", left)
root.bind("<Right>", right)
root.bind("<Up>", up)
root.bind("<Down>", down)
root.mainloop()