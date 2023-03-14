from tkinter import *
from PIL import ImageTk,Image
import json

currentDir = "north"
currentPos = "(0, 0)"

def left(event):
    if currentDir == "north":
        currentDir = "west"
        ImageTk.PhotoImage(Image.open(map[currentPos][currentDir]["IMG"]))
    elif currentDir == "east":
        currentDir = "north"
        ImageTk.PhotoImage(Image.open(map[currentPos][currentDir]["IMG"]))
    elif currentDir == "south":
        currentDir = "east"
        ImageTk.PhotoImage(Image.open(map[currentPos][currentDir]["IMG"]))
    elif currentDir == "west":
        currentDir = "south"
        ImageTk.PhotoImage(Image.open(map[currentPos][currentDir]["IMG"]))


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