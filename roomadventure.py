# name: Logan Coker 
# date: 3/29/23
# description: room thing 

from tkinter import * 
from item import *



class Room:
    """A room has a name and a filepath that points to a .gif image."""

    def __init__(self, name:str, imageFilepath:str) -> None:
        self.name = name
        self.image = imageFilepath
        self.exits = {} 
        self.items: list[Item] = []
        self.itemNames: list[str] = []    


    def addExit(self, label:str, room:'Room'): 
        self.exits[label] = room
    

    def addItem(self, item:Item):
        self.items.append(item) 
    
    def addItemNames(self):
        for item in self.items:
            self.itemNames.append(item.name)

    

    def __str__(self) -> str:
        result = f'You are in {self.name}\n'

        result += 'You see: '
        for item in self.itemNames:
            result += item + ', '
        result += '\n'

        result += 'Exits: '
        for exits in self.exits.keys():
            result += exits + ', '
        result += '\n'

        return result
        


class Game(Frame):

    EXIT_ACTIONS = ['quit', 'exit', 'q']

    # statuses
    STATUS_DEFALT = 'I don\'t understand'
    STATUS_DEATH = '*dies*'
    STATUS_BAD_EXIT = 'Invalid Exit'
    STATUS_ROOM_CHANGE = 'Room Changed'
    STATUS_GRABBED = 'Item Grabbed'
    STATUS_BAD_GRABS = 'I can\'t grab'
    STATUS_BAD_ITEM = 'I don\'t see'

    WIDTH = 800
    HEIGHT = 600

    def __init__(self, parent) -> None:
        self.inventory = []
        Frame.__init__(self, parent)
        self.pack(fill=BOTH, expand=1)
    

    def setupGame(self):
        # create room
        r1 = Room('Room 1', 'room1.gif')
        r2 = Room('Room 2', 'room2.gif')
        r3 = Room('Room 3', 'room3.gif')
        r4 = Room('Room 4', 'room4.gif')
        rooms = [r1, r2, r3, r4]


        # add exits
        r1.addExit('east', r2)
        r1.addExit('south', r3)

        r2.addExit('west', r1)
        r2.addExit('south', r4)

        r3.addExit('north', r1)
        r3.addExit('east', r4)

        r4.addExit('north', r2)
        r4.addExit('west', r3)
        r4.addExit('south', None) 

        # add items 
        r1.addItem(chair)
        r1.addItem(chair)
        r1.addItem(key)

        r2.addItem(table)
        r2.addItem(bookcase)
        r2.addItem(book)

        r3.addItem(bookcase)
        # r3.addItem('dimsbale_dimmadome', 'Owned by Doug Dimmadome, onwer of the Dimsdale Dimmodme')
        r3.addItem(debris)

        r4.addItem(table)
        r4.addItem(crois)
        
        for room in rooms:
            room.addItemNames()

        # set current room
        self.currentRoom = r1
        

    def setupGUI(self):
        # input
        self.playerInput = Entry(self, bg='white', fg='black')
        self.playerInput.bind('<Return>', self.process) 
        self.playerInput.pack(side=BOTTOM, fill=X)
        self.playerInput.focus()

        # image 
        img = None
        self.imageContainer = Label(self, width=Game.WIDTH//2, image=img)
        self.imageContainer.image = img
        self.imageContainer.pack(side=LEFT, fill=Y)
        self.imageContainer.pack_propagate(False)

        # text
        textContainer = Frame(self, width=Game.WIDTH//2)
        self.text = Text(textContainer, bg='lightgrey', fg='black', state=DISABLED)
        self.text.pack(fill=Y, expand=1) 
        textContainer.pack(side=RIGHT, fill=Y) 
        textContainer.pack_propagate(False) 


    def setRoomImage(self):
        if self.currentRoom == None:
            img = PhotoImage(file='skull.gif')
        else:
            img = PhotoImage(file=self.currentRoom.image)
        
        self.imageContainer.config(image=img)
        self.imageContainer.image = img


    def setStatus(self, status):
        self.text.config(state=NORMAL)
        self.text.delete(1.0, END)

        if self.currentRoom == None:
            self.text.insert(END, Game.STATUS_DEATH)
        else:
            content = f'{self.currentRoom}\nYou are carrying:{self.inventory}\n\n{status}'
            self.text.insert(END, content)
        
        self.text.config(state=DISABLED) 


    def clearEntery(self):
        self.playerInput.delete(0,END)


    def handleGo(self, dest):
        status = Game.STATUS_BAD_EXIT

        if dest in self.currentRoom.exits:
            self.currentRoom = self.currentRoom.exits[dest]
            status = Game.STATUS_ROOM_CHANGE
        
        self.setStatus(status)
        self.setRoomImage()


    def handleLook(self, item:str):
        status = Game.STATUS_BAD_ITEM


        if item in allItemsStrList and item in self.currentRoom.itemNames:
            index = allItemsStrList.index(item) 
            iteM:Item = allItemList[index] 
            status = iteM.description
        

        self.setStatus(status)


    def handleTake(self, grabs):
        status = Game.STATUS_BAD_GRABS

        if grabs in allItemsStrList and grabs in self.currentRoom.itemNames:
            index = allItemsStrList.index(grabs) 
            iteM:Item = allItemList[index] 
            if iteM.grabbable:
                self.currentRoom.items.remove(iteM)
                self.currentRoom.itemNames.remove(str(iteM))
                self.inventory.append(str(iteM))
                status = Game.STATUS_GRABBED

        
        self.setStatus(status)


    def play(self):
        self.setupGame()
        self.setupGUI()
        self.setRoomImage()
        self.setStatus('')


    def process(self, event):
        action = self.playerInput.get()
        action = action.lower()
        
        if action in Game.EXIT_ACTIONS:
            exit()

        if self.currentRoom == None:
            self.clearEntery()
            return 
        
        words = action.split()
        
        if len(words) != 2:
            self.setStatus(Game.STATUS_DEFALT)
            return 
        
        self.clearEntery()

        verb = words[0]
        noun = words[1]

        match verb:
            case 'go':
                self.handleGo(dest=noun)

            case 'look':
                self.handleLook(item=noun)

            case 'take':
                self.handleTake(grabs=noun)

            
window = Tk()
window.title('Room Adventure... RevOluTionS')
game = Game(window)
game.play()
window.mainloop()
