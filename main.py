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
    if currentDir == "north":
        currentPos = map[currentPos][currentDir]["next_area"]
        img = ImageTk.PhotoImage(Image.open(map[currentPos][currentDir]["IMG"]))
        myLabel.configure(image=img)
        myLabel.image = img
    elif currentDir == "south":
        currentPos = map[currentPos][currentDir]["prev_area"]
        img = ImageTk.PhotoImage(Image.open(map[currentPos][currentDir]["IMG"]))
        myLabel.configure(image=img)
        myLabel.image = img
    else:
        print("Can't go that way.")

def down(event):
    global currentDir, myLabel, currentPos
    if currentDir == "north":
        currentPos = map[currentPos][currentDir]["prev_area"]
        img = ImageTk.PhotoImage(Image.open(map[currentPos][currentDir]["IMG"]))
        myLabel.configure(image=img)
        myLabel.image = img
    elif currentDir == "south":
        currentPos = map[currentPos][currentDir]["next_area"]
        img = ImageTk.PhotoImage(Image.open(map[currentPos][currentDir]["IMG"]))
        myLabel.configure(image=img)
        myLabel.image = img
    else:
        print("Can't go that way.")

m = open("map.json")
map = json.load(m)
root = Tk()
myImg = ImageTk.PhotoImage(Image.open(map[currentPos][currentDir]["IMG"]))
myLabel = Label(image = myImg)

compassImg = Image.open("imgs/compass/faceNorth.png")
resizeCompass = compassImg.resize((100, 100), Image.ANTIALIAS)
newCompass = ImageTk.PhotoImage(resizeCompass)
compassLabel = Label(image = newCompass)

myLabel.place(x=0, y=0)
compassLabel.place(x=0, y=0)
root.bind("<Left>", left)
root.bind("<Right>", right)
root.bind("<Up>", up)
root.bind("<Down>", down)

root.mainloop()