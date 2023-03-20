# Importing the necessary things in order to run the program
from tkinter import *
from PIL import ImageTk,Image
import json
from tkinter import messagebox

# Initializing starting states
currentDir = "north" # you will start facing north
currentPos = "(0, 0)" # you will start in the bottom left corner of the map
# This function fits inside the changeCompass function, this is
# where the compass image is actually replaced and updated.
def configureCompass(temp):
    global compassLabel
    temp2 = temp.resize((50, 50), Image.Resampling.LANCZOS) # resizing the image
    updateCompass = ImageTk.PhotoImage(temp2)
    compassLabel.configure(image=updateCompass)
    compassLabel.image = updateCompass # updating the compass

# Function to replace the compass image in the corner of the screen to match
# the direction that you are facing. The replacing is done in the configureCompass
# function, this function is for grabbing the necessary compass image and then sending it
# to the configureCompass function.
def changeCompass(currentDir):
    if currentDir == "north": # matches condition with direction
        temp = Image.open("imgs/compass/faceNorth.png") # grabbing image path
        configureCompass(temp) # sending the image to be replaced
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
    global img, canvas, text
    img = Image.open(map[currentPos][currentDir]["IMG"]).convert("RGBA")
    img = img.resize((canvas.winfo_width(), canvas.winfo_height()), Image.Resampling.LANCZOS)
    # ^^ This line resizes the image so it will load faster
    img = ImageTk.PhotoImage(img)
    canvas.create_image(0, 0, image = img, anchor="nw") # creating a new image to replace the old one

# Function for turning left
def left(event):
    global currentDir
    # The function gets your current position and direction and
    # replaces the image with the next respective image
    if currentDir == "north":
        currentDir = "west"
        replace(currentDir, currentPos)
        changeCompass(currentDir) # each time you move, it updates the compass
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
        if(cantGoForwards(currentPos, currentDir)):
            popup()
        else:
            currentPos = map[currentPos][currentDir]["next_area"]
            replace(currentDir, currentPos)
    elif currentDir == "east":
        if(cantGoForwards(currentPos, currentDir)):
            popup()
        else:
            currentPos = map[currentPos][currentDir]["next_area"]
            replace(currentDir, currentPos)
    elif currentDir == "south":
        if(cantGoBack(currentPos, currentDir)):
            popup()
        else:
            currentPos = map[currentPos][currentDir]["prev_area"]
            replace(currentDir, currentPos)
    elif currentDir == "west":
        if(cantGoBack(currentPos, currentDir)):
            popup()
        else:
            currentPos = map[currentPos][currentDir]["prev_area"]
            replace(currentDir, currentPos)

# Function for moving backwards
def down(event):
    global currentDir, currentPos
    if currentDir == "north":
        if(cantGoBack(currentPos, currentDir)):
            popup()
        else:
            currentPos = map[currentPos][currentDir]["prev_area"]
            replace(currentDir, currentPos)
    elif currentDir == "east":
        if(cantGoBack(currentPos, currentDir)):
            popup()
        else:
            currentPos = map[currentPos][currentDir]["prev_area"]
            replace(currentDir, currentPos)
    elif currentDir == "south":
        if(cantGoForwards(currentPos, currentDir)):
            popup()
        else:
            currentPos = map[currentPos][currentDir]["next_area"]
            replace(currentDir, currentPos)
    elif currentDir == "west":
        if(cantGoForwards(currentPos, currentDir)):
            popup()
        else:
            currentPos = map[currentPos][currentDir]["next_area"]
            replace(currentDir, currentPos)

# This function will check if there is a wall behind you
def cantGoBack(pos, dir):
    if map[pos][dir]["prev_area"] == "none":
        return TRUE
    else:
        return FALSE

# This function will check if there is a wall in front of you
def cantGoForwards(pos, dir):
    if map[pos][dir]["next_area"] == "none":
        return TRUE
    else:
        return FALSE
    
# This function will get the player's current position and display the image
# for their respective position and direction that they are facing
# This is mainly meant to resize the image that first appears when running
# the program, since without this function it will be displayed at its
# original size.
def resizer(e):
    global img, currentPos, currentDir
    img = Image.open(map[currentPos][currentDir]["IMG"])
    img = img.resize((e.width, e.height), Image.Resampling.LANCZOS)
    img = ImageTk.PhotoImage(img)
    canvas.create_image(0, 0, image = img, anchor="nw")

# This function will make a notification pop up if you can't go a certain direction
def popup():
    pop = messagebox.showinfo("Notification", "You can't go that way.")
# When you press ok on the notification popup, it returns an "ok" message.
# These two lines below make it so that it doesn't show up at the bottom
# of your screen when you're playing.
    if pop == "ok":
        return NONE
    Label(root, text=pop).pack()

# Initializing and opening the map json file
m = open("map.json")
map = json.load(m)

# Initializing a canvas and making the starting image the background image
root = Tk()
img = Image.open(map[currentPos][currentDir]["IMG"]) # out current position is (0, 0)
img2 = img.resize((1344, 653), Image.Resampling.LANCZOS)
# ^^ the original images are 4032 x 1960, so I resized the canvas to 1/3 of its original size to reduce loading time
img3 = ImageTk.PhotoImage(img2)
canvas = Canvas(root, width = 1344, height = 653) # making the canvas the same size as the photos
canvas.pack(fill="both", expand=TRUE)
canvas.create_image(0, 0, image = img3, anchor="nw") # setting the image as the background image

# Initiallizing the compass, you start facing north
compassImg = Image.open("imgs/compass/faceNorth.png").convert("RGBA")
resizeCompass = compassImg.resize((50, 50), Image.Resampling.LANCZOS)
newCompass = ImageTk.PhotoImage(resizeCompass)
compassLabel = Label(image = newCompass)

# Placing the compass on top of the background image
compassLabel.place(x=0, y=0)

# This line resizes the window to match the height
# and width of the background image so you don't have to resize
root.geometry('{}x{}'.format(img3.width(), img3.height()))

# Binding the arrow keys to the functions initialized earlier
root.bind("<Left>", left)
root.bind("<Right>", right)
root.bind("<Up>", up)
root.bind("<Down>", down)
root.title("2.5D Game")
root.bind("<Configure>", resizer)
root.mainloop()