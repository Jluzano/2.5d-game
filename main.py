from tkinter import *
from PIL import ImageTk,Image
import json

# Initializing current states
currentDir = "north"
currentPos = "(0, 0)"
# Function to replace the current compass image with corresponding compass image
def configureCompass(temp):
    global compassLabel
    temp2 = temp.resize((50, 50), Image.Resampling.LANCZOS)
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
    global img, canvas
    img = Image.open(map[currentPos][currentDir]["IMG"]).convert("RGBA")
    img = img.resize((canvas.winfo_width(), canvas.winfo_height()), Image.Resampling.LANCZOS)
    img = ImageTk.PhotoImage(img)
    canvas.create_image(0, 0, image = img, anchor="nw")

# Function for turning left
def left(event):
    global currentDir
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
    global currentDir
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
    global currentDir, currentPos
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
    global currentDir, currentPos
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

def resizer(e):
    global img, currentPos, currentDir
    img = Image.open(map[currentPos][currentDir]["IMG"])
    img = img.resize((e.width, e.height), Image.Resampling.LANCZOS)
    img = ImageTk.PhotoImage(img)
    canvas.create_image(0, 0, image = img, anchor="nw")

# Initializing the map json file
m = open("map.json")
map = json.load(m)

# Initializing the background image
root = Tk()
img = Image.open(map[currentPos][currentDir]["IMG"])
img2 = img.resize((1344, 653), Image.Resampling.LANCZOS)
img3 = ImageTk.PhotoImage(img2)
canvas = Canvas(root, width = 1344, height = 653)
canvas.pack(fill="both", expand=TRUE)
canvas.create_image(0, 0, image = img3, anchor="nw")

# Initiallizing the compass, you start facing north
compassImg = Image.open("imgs/compass/faceNorth.png").convert("RGBA")
resizeCompass = compassImg.resize((50, 50), Image.Resampling.LANCZOS)
newCompass = ImageTk.PhotoImage(resizeCompass)
compassLabel = Label(image = newCompass)

# Placing the compass on top of the background image
compassLabel.place(x=0, y=0)

# This line resizes the window to match the height
# and width of the background image so you don't have to resize
root.geometry('{}x{}'.format(int(img2.width()/3), int(img2.height()/3)))

# Binding the arrow keys to functions initialized earlier
root.bind("<Left>", left)
root.bind("<Right>", right)
root.bind("<Up>", up)
root.bind("<Down>", down)
root.title("2.5D Game")
root.bind("<Configure>", resizer)
root.mainloop()