from tkinter import *
from game import *

Reset = False



class End(Frame):

    def __init__(self, parent):
        self.parent = parent
        Frame.__init__(self, parent)
        self.setupGUI()
        self.Error = False
        self.Reset = False

        # if Game.status == "You couldn't take the thought of food any longer.":
    
    def croissantGUI(self):
        self.f1 = Frame(self)
        self.display = Label(
            self.f1, 
            text="You couldn't take the thought of food any longer.\nYou have died.",
            anchor=E,
            bg="black",
            fg="red",
            font=("TimesNewRoman", 20))
        

        self.button1 = Button(
            self.f1,
            text="Quit",
            bg="black",
            fg="red",
            command=quit
        )
            
        self.pack()
        self.f1.pack()
        self.display.pack(fill=Y)
        self.button1.pack()
    

    def keyGUI(self):
        self.f1 = Frame(self)
        self.display = Label(
            self.f1, 
            text="You idiot! How can you leave without the key??!",
            anchor=E,
            bg="white",
            fg="black",
            font=("TimesNewRoman", 20))
        

        self.button1 = Button(
            self.f1,
            text="Quit",
            bg="white",
            fg="black",
            command=quit
        )
            
        self.pack()
        self.f1.pack()
        self.display.pack(fill=Y)
        self.button1.pack()

    
    def firstwinGUI(self):
        self.f1 = Frame(self)
        self.display = Label(
            self.f1, 
            text="Well done! You have the key and were able to escape!",
            anchor=E,
            bg="white",
            fg="blue",
            font=("TimesNewRoman", 20))
        

        self.button1 = Button(
            self.f1,
            text="Quit",
            bg="white",
            fg="black",
            command=quit
        )
            
        self.pack()
        self.f1.pack()
        self.display.pack(fill=Y)
        self.button1.pack()

    def secretwinGUI(self):
        self.f1 = Frame(self)
        self.display = Label(
            self.f1, 
            text="Good choice! Congratulations you have chosen the right door and have escaped!",
            anchor=E,
            bg="white",
            fg="blue",
            font=("TimesNewRoman", 20))
        

        self.button1 = Button(
            self.f1,
            text="Quit",
            bg="white",
            fg="black",
            command=quit
        )
            
        self.pack()
        self.f1.pack()
        self.display.pack(fill=Y)
        self.button1.pack()

    