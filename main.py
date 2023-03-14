from tkinter import *
from PIL import ImageTk,Image
import json

currentDir = "north"
currentPos = "(0, 0)"

def left(event):
    global currentDir
    global myLabel
    if currentDir == "north":
        currentDir = "west"
        img = ImageTk.PhotoImage(Image.open(map[currentPos][currentDir]["IMG"]))
        myLabel.configure(image=img)
        myLabel.image = img
    elif currentDir == "east":
        currentDir = "north"
        img = ImageTk.PhotoImage(Image.open(map[currentPos][currentDir]["IMG"]))
        myLabel.configure(image=img)
        myLabel.image = img
    elif currentDir == "south":
        currentDir = "east"
        img = ImageTk.PhotoImage(Image.open(map[currentPos][currentDir]["IMG"]))
        myLabel.configure(image=img)
        myLabel.image = img
    elif currentDir == "west":
        currentDir = "south"
        img = ImageTk.PhotoImage(Image.open(map[currentPos][currentDir]["IMG"]))
        myLabel.configure(image=img)
        myLabel.image = img


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