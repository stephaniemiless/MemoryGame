# =======================================
# Stephanie and Kelly (Team Skelly)
# COMP123-04 Fall 2022 Final Project
# Sea Life Memory Game
# ======================================= import statements
import tkinter as tk
import random
import PIL.Image as Image
import PIL.ImageTk as ImageTk
# ======================================= class def

class MemoryGame:
    """Creates a canvas with 20 rectangle objects and image
    objects. Allows the user to click on the tiles and
    checks to see if the ids are the same. It changes the
    placements of the images and rectangles based on when
    they are clicked and whether a successful match has
    taken place. Destroys the window once the game is over."""
    
    def __init__(self):
        #initialize window size and title
        self.window = tk.Tk()
        self.window.title("Sea Life Memory Game")
        self.window.minsize(590, 600)
        self.window.maxsize(590, 600)

        #set main canvas as background and bind mouse click
        self.canvas = tk.Canvas(self.window, bg="lightblue",
                                bd=0, highlightthickness=0,
                                width=590, height=600)
        self.canvas.grid(row=0, column=0)
        self.canvas.bind("<Button-1>", self.chooseTile)

        #establish coordinates for tiles and shuffle image placement
        coordinates = [(5,30,105,130), (5,160,105,260), (5,290,105,390), (5,420,105,520), (125,30,225,130), (125,160,225,260), (125,290,225,390), (125,420,225,520), (245,30,345,130), (245,160,345,260), (245,290,345,390), (245,420,345,520), (365,30,465,130), (365,160,465,260), (365,290,465,390), (365,420,465,520), (485,30,585,130), (485,160,585,260), (485,290,585,390), (485,420,585,520)]
        imageChoices = ['cropped images/001-turtle.png','cropped images/007-blowfish.png','cropped images/010-jellyfish.png','cropped images/011-starfish.png','cropped images/018-lobster.png','cropped images/028-fish.png','cropped images/033-walrus.png','cropped images/042-goldfish.png','cropped images/045-seal.png','cropped images/046-penguin.png']
        random.shuffle(coordinates)

        #write title to top of canvas
        self.canvas.create_text(295, 15, text="Sea Life Memory Game!",
                                anchor="center", fill="white",
                                font="Times 24 bold")


        #initialize counts and define collection list
        coordinateCount = 0
        imageCount = 0
        self.imageCollection = []

        #for loop to attach images to each rectangle on the canvas
        for i in range(len(imageChoices)):
            x1, y1, x2, y2 = coordinates[coordinateCount] #sets coordinates
            self.image = ImageTk.PhotoImage(Image.open(imageChoices[imageCount])) #creates image
            self.image.img = self.image
            self.id = self.canvas.create_image(x1, y1, anchor="nw",
                                    image=self.image.img) #adds image to canvas
            self.imageCollection.append(self.id) #adds image id to the list
            self.canvas.create_rectangle(x1, y1, x2, y2, fill="white", outline="white")
            coordinateCount += 1 #updates count for next iteration of a new coordinate position
            x1, y1, x2, y2 = coordinates[coordinateCount] #sets new coordinate position
            self.id = self.canvas.create_image(x1, y1, anchor="nw",
                                               image=self.image.img) #places same image on new canvas (we need two instances of an image but in different places)
            self.canvas.create_rectangle(x1, y1, x2, y2, fill="white", outline="white")

            #update counts
            coordinateCount += 1
            imageCount += 1

            self.imageCollection.append(self.id) #adds image id to the list

        #create instructional text
        self.canvas.create_text(295, 550, text="Find all the pairs as fast as possible.",
                                fill="white", font="Times 18", anchor="center")
        self.canvas.create_text(295, 570, text="Click on a card to turn it over and find the same matching card.",
                                fill="white", font="Times 18", anchor="center")


    def run(self):
        """Updates the window"""
        self.window.mainloop()

    #defining global lists for chooseTile function
    global lst
    lst = []
    global matches
    matches = 0

    def chooseTile(self, event):
        """This function is designed to be a callback function that is bound
        to a mouse click. It is written for two clicks, and will reset after the two clicks
        have been made. On the first click, the function will collect the x and y coordinates of
        whatever place the mouse had clicked on. Then using those coordinates, the function will
        find any canvas object that is overlapping the given coordinates and append that value to
        the global list. Because this function is written to consider two different clicks, there are
        conditional statements to determine which click we are on (with reference to the global list).
        If the length of the list is less than two (meaning only one click has been made), the function will
        move the rectangle object under the image object and wait for a second click. On the second click,
        the function does the same as it did for the first click and appends an overlapping object to the list. So,
        now that the list has two objects, the function will move the second rectangle object under the image. Now, with
        both images being shown, the function will check to see if the image ids are the same. If they are the same, nothing
        will happen to the objects (they remain face up), but the function will add 2 to our matches counter and clear
        the list. If the image ids do not match, both object rectangles will be placed above each image, and the list will
        still be cleared as well to restart the process. Once the match count reaches 20 (all have been matched),
        the game window will self-destruct."""
        global lst
        global matches
        x = event.x
        y = event.y
        item = self.canvas.find_overlapping(x-1,y-1,x+1,y+1)
        lst.append(item)
        if item == ():
            #this will ensure that if the user clicks on the background, the game window self-destructs
            self.window.destroy()
        elif len(lst) < 2:
                self.canvas.tag_lower(lst[0][1], lst[0][0])
        elif len(lst) == 2:
            self.canvas.tag_lower(lst[1][1],lst[1][0])
            if self.canvas.itemcget(lst[0][0], "image") == self.canvas.itemcget(lst[1][0], "image"):
                matches += 2
                lst.clear()
            else:
                self.window.update_idletasks()
                self.window.after(1500)
                self.canvas.lower(lst[0][0], lst[0][1])
                self.canvas.lower(lst[1][0], lst[1][1])
                lst.clear()
        if matches == 20:
            self.window.update_idletasks()
            self.window.after(1000)
            self.window.destroy()


# ======================================= script calls

game = MemoryGame()
game.run()

# ======================================= test calls
# due to the nature of our project, we relied on user testing in place of traditional unit and scripted tests
