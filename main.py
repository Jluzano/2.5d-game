from tkinter import *
from PIL import ImageTk,Image
import json

m = open("map.json")
map = json.load(m)
root = Tk()
myImg = ImageTk.PhotoImage(Image.open(map["(0, 0)"]["north"]["IMG"]))
myLabel = Label(image = myImg)
myLabel.pack()
root.mainloop()