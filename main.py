from tkinter import *
from PIL import ImageTk,Image
import json

currentDir = "north"
currentPos = "(0, 0)"
def replace(currentDir, currentPos):
    img = ImageTk.PhotoImage(Image.open(map[currentPos][currentDir]["IMG"]))
    myLabel.configure(image=img)
    myLabel.image = img

def left(event):
    global currentDir, myLabel
    if currentDir == "north":
        currentDir = "west"
        replace(currentDir, currentPos)
    elif currentDir == "east":
        currentDir = "north"
        replace(currentDir, currentPos)
    elif currentDir == "south":
        currentDir = "east"
        replace(currentDir, currentPos)
    elif currentDir == "west":
        currentDir = "south"
        replace(currentDir, currentPos)

def right(event):
    global currentDir, myLabel
    if currentDir == "north":
        currentDir = "east"
        replace(currentDir, currentPos)
    elif currentDir == "east":
        currentDir = "south"
        replace(currentDir, currentPos)
    elif currentDir == "south":
        currentDir = "west"
        replace(currentDir, currentPos)
    elif currentDir == "west":
        currentDir = "north"
        replace(currentDir, currentPos)

def up(event):
    global currentDir, myLabel, currentPos
    currentPos = map[currentPos]["next_area"]
    img = ImageTk.PhotoImage(Image.open(map[currentPos]["north"]["IMG"]))
    myLabel.configure(image=img)
    myLabel.image = img

m = open("map.json")
map = json.load(m)
root = Tk()
myImg = ImageTk.PhotoImage(Image.open(map[currentPos][currentDir]["IMG"]))
myLabel = Label(image = myImg)
myLabel.pack()
root.bind("<Left>", left)
root.bind("<Right>", right)
root.bind("<Up>", up)
'''
root.bind("<Down>", down)
'''
root.mainloop()