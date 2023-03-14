from tkinter import *
from PIL import ImageTk,Image
import json

currentDir = "north"
currentPos = "(0, 0)"
def testFunction(currentDir, currentPos):
    img = ImageTk.PhotoImage(Image.open(map[currentPos][currentDir]["IMG"]))
    myLabel.configure(image=img)
    myLabel.image = img

def left(event):
    global currentDir
    global myLabel
    if currentDir == "north":
        currentDir = "west"
        testFunction(currentDir, currentPos)
    elif currentDir == "east":
        currentDir = "north"
        testFunction(currentDir, currentPos)
    elif currentDir == "south":
        currentDir = "east"
        testFunction(currentDir, currentPos)
    elif currentDir == "west":
        currentDir = "south"
        testFunction(currentDir, currentPos)


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