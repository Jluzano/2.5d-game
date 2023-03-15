from tkinter import *
from PIL import ImageTk,Image
import json

# Initializing current states
currentDir = "north"
currentPos = "(0, 0)"
# Function to replace the current compass image with corresponding compass image
def configureCompass(temp):
    global compassLabel
    temp2 = temp.resize((50, 50), Image.ANTIALIAS)
    updateCompass = ImageTk.PhotoImage(temp2)
    compassLabel.configure(image=updateCompass)
    compassLabel.image = updateCompass

# Function to replace the actual compass image in the corner of the screen
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
    img = ImageTk.PhotoImage(Image.open(map[currentPos][currentDir]["IMG"]).convert("RGBA"))
    myLabel.configure(image=img)
    myLabel.image = img

# Function for turning left
def left(event):
    global currentDir, myLabel
    # The function gets your current position and direction and
    # replaces the image with the next respective image
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

# Function for turning right
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

# Function for moving forwards
def up(event):
    global currentDir, myLabel, currentPos
    if currentDir == "north":
        currentPos = map[currentPos][currentDir]["next_area"]
        replace(currentDir, currentPos)
    elif currentDir == "east":
        currentPos = map[currentPos][currentDir]["next_area"]
        replace(currentDir, currentPos)
    elif currentDir == "south":
        currentPos = map[currentPos][currentDir]["prev_area"]
        replace(currentDir, currentPos)
    elif currentDir == "west":
        currentPos = map[currentPos][currentDir]["prev_area"]
        replace(currentDir, currentPos)

# Function for moving backwards
def down(event):
    global currentDir, myLabel, currentPos
    if currentDir == "north":
        currentPos = map[currentPos][currentDir]["prev_area"]
        replace(currentDir, currentPos)
    elif currentDir == "east":
        currentPos = map[currentPos][currentDir]["prev_area"]
        replace(currentDir, currentPos)
    elif currentDir == "south":
        currentPos = map[currentPos][currentDir]["next_area"]
        replace(currentDir, currentPos)
    elif currentDir == "west":
        currentPos = map[currentPos][currentDir]["next_area"]
        replace(currentDir, currentPos)

# Initializing the map json file
m = open("map.json")
map = json.load(m)

# Initializing the background image
root = Tk()
myImg = ImageTk.PhotoImage(Image.open(map[currentPos][currentDir]["IMG"]))
myLabel = Label(image = myImg)

# Initiallizing the compass, you start facing north
compassImg = Image.open("imgs/compass/faceNorth.png").convert("RGBA")
resizeCompass = compassImg.resize((50, 50), Image.ANTIALIAS)
newCompass = ImageTk.PhotoImage(resizeCompass)
compassLabel = Label(image = newCompass)

#Initializing the player map
mapImg = Image.open("imgs/compass/playerMap.png").convert("RGBA")
resizeMap = mapImg.resize((80, 80), Image.ANTIALIAS)
newMap = ImageTk.PhotoImage(resizeMap)
mapLabel = Label(image = newMap)

# Placing the compass on top of the background image
myLabel.place(x=0, y=0)
compassLabel.place(x=0, y=0)
mapLabel.place(x = myImg.width(), y = 0)

# This line resizes the window to match the height
# and width of the background image so you don't have to resize
root.geometry('{}x{}'.format(myImg.width(), myImg.height()))

# Binding the arrow keys to functions initialized earlier
root.bind("<Left>", left)
root.bind("<Right>", right)
root.bind("<Up>", up)
root.bind("<Down>", down)
root.title("2.5D Game")
root.mainloop()