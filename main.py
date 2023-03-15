from tkinter import *
from PIL import ImageTk,Image
import json

currentDir = "north"
currentPos = "(0, 0)"

def configureCompass(temp):
    global compassLabel
    temp2 = temp.resize((50, 50), Image.ANTIALIAS)
    updateCompass = ImageTk.PhotoImage(temp2)
    compassLabel.configure(image=updateCompass)
    compassLabel.image = updateCompass

def changeCompass(currentDir):
    if currentDir == "north":
        temp = Image.open("imgs/compass/faceNorth.png")
        configureCompass(temp)
    elif currentDir == "east":
        temp = Image.open("imgs/compass/faceEast.png")
        configureCompass(temp)
    elif currentDir == "south":
        temp = Image.open("imgs/compass/faceSouth.png")
        configureCompass(temp)
    elif currentDir == "west":
        temp = Image.open("imgs/compass/faceWest.png")
        configureCompass(temp)

# Function to replace the current image with the next image
def replace(currentDir, currentPos):
    img = ImageTk.PhotoImage(Image.open(map[currentPos][currentDir]["IMG"]))
    myLabel.configure(image=img)
    myLabel.image = img

# Function 
def left(event):
    global currentDir, myLabel
    if currentDir == "north":
        currentDir = "west"
        replace(currentDir, currentPos)
        changeCompass(currentDir)
    elif currentDir == "east":
        currentDir = "north"
        replace(currentDir, currentPos)
        changeCompass(currentDir)
    elif currentDir == "south":
        currentDir = "east"
        replace(currentDir, currentPos)
        changeCompass(currentDir)
    elif currentDir == "west":
        currentDir = "south"
        replace(currentDir, currentPos)
        changeCompass(currentDir)

def right(event):
    global currentDir, myLabel
    if currentDir == "north":
        currentDir = "east"
        replace(currentDir, currentPos)
        changeCompass(currentDir)
    elif currentDir == "east":
        currentDir = "south"
        replace(currentDir, currentPos)
        changeCompass(currentDir)
    elif currentDir == "south":
        currentDir = "west"
        replace(currentDir, currentPos)
        changeCompass(currentDir)
    elif currentDir == "west":
        currentDir = "north"
        replace(currentDir, currentPos)
        changeCompass(currentDir)

def up(event):
    global currentDir, myLabel, currentPos
    if currentDir == "north":
        currentPos = map[currentPos][currentDir]["next_area"]
        replace(currentDir, currentPos)
    elif currentDir == "south":
        currentPos = map[currentPos][currentDir]["prev_area"]
        replace(currentDir, currentPos)

def down(event):
    global currentDir, myLabel, currentPos
    if currentDir == "north":
        currentPos = map[currentPos][currentDir]["prev_area"]
        replace(currentDir, currentPos)
    elif currentDir == "south":
        currentPos = map[currentPos][currentDir]["next_area"]
        replace(currentDir, currentPos)
        
# Initializing the map json file
m = open("map.json")
map = json.load(m)
# Initializing the background image
root = Tk()
myImg = ImageTk.PhotoImage(Image.open(map[currentPos][currentDir]["IMG"]))
myLabel = Label(image = myImg)
# Initiallizing the compass
compassImg = Image.open("imgs/compass/faceNorth.png")
resizeCompass = compassImg.resize((50, 50), Image.ANTIALIAS)
newCompass = ImageTk.PhotoImage(resizeCompass)
compassLabel = Label(image = newCompass)
# Placing the compass on top of the background image
myLabel.place(x=0, y=0)
compassLabel.place(x=0, y=0)
# This line resizes the window to match the height and width of the background image
root.geometry('{}x{}'.format(myImg.width(), myImg.height()))
# Binding the arrow keys to functions initialized earlier
root.bind("<Left>", left)
root.bind("<Right>", right)
root.bind("<Up>", up)
root.bind("<Down>", down)
root.mainloop()