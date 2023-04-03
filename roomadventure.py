# name: Logan Coker 
# date: 3/29/23
# description: room thing 

from tkinter import * 



class Room:
    """A room has a name and a filepath that points to a .gif image."""

    def __init__(self, name:str, imageFilepath:str) -> None:
        self.name = name
        self.image = imageFilepath
        self.exits = {} 
        self.items = {}
        self.grabbables = [] 

    def addExit(self, label:str, room:'Room'): 
        self.exits[label] = room
    
    def addItem(self, label:str, desc:str):
        self.items[label] = desc 

    def addGrabs(self, grab:str):
        self.grabbables.append(grab)

    def delGrab(self, grab:str):
        self.grabbables.remove(grab)
    
    def __str__(self) -> str:
        result = f'You are in {self.name}\n'

        result += 'You see: '
        for item in self.items.keys():
            result += item + ' '
        result += '\n'

        result += 'Exits: '
        for exits in self.exits.keys():
            resutl += exits + ' '
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
        r1.addItem('chair', 'legs')
        r1.addItem('more chair', 'some leg')

        r2.addItem('fire place', 'fire.exe running')
        r2.addItem('extraChair', 'with leg')

        r3.addItem('desk', 'made of broken chair')
        r3.addItem('dimsbale_dimmadome', 'Owned by Doug Dimmadome, onwer of the Dimsdale Dimmodme')
        r3.addItem('chair.exe', 'stoped working')

        r4.addItem('croissant', 'butter')


        # grabs

        # set current room
        pass

    def setupGUI(self):
        pass

    def setRoomImage(self):
        pass

    def setStatus(self):
        pass

    def clearEntery(self):
        pass

    def handleGo(self):
        pass

    def handleTake(self):
        pass

    def handleLook(self):
        pass

    def play(self):
        pass

    def process(self, event):
        pass

