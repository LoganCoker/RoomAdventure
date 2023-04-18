from tkinter import *


class End(Frame):

    def __init__(self, parent):
        self.parent = parent
        Frame.__init__(self, parent)
        self.setupGUI()
        self.Error = False

        # if Game.status == "You couldn't take the thought of food any longer.":
    
    def setupGUI(self):
        self.f1 = Frame(self)
        self.display = Label(
            self.f1, 
            text="You couldn't take the thought of food any longer.\nYou have died.",
            anchor=E,
            bg="white",
            fg="black",
            font=("TimesNewRoman", 20))
        
        self.button1 = Button(
            self.f1,
            text="Restart",
            bg="white",
            fg="black",
            command=self.restart
        )

        self.button2 = Button(
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
        self.button2.pack()
    
    def restart(self):
            print("Restarting")

end = Tk()
end.title("End screen")
end.geometry(f'{600}x{600}')
