from tkinter import *
from PIL import ImageTk,Image
import json

def left(event):
    currentDir = map[currentPos]["left"]
    ImageTk.PhotoImage(Image.open(currentDir))

currentDir = "north"
currentPos = "(0, 0)"
m = open("map.json")
map = json.load(m)
root = Tk()
myImg = ImageTk.PhotoImage(Image.open(map[currentPos][currentDir]["IMG"]))
myLabel = Label(image = myImg)
myLabel.pack()
root.bind("<Left>", left)
'''
root.bind("<Right>", right)
root.bind("<Up>", up)
root.bind("<Down>", down)
'''
root.mainloop()