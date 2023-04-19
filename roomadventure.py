from tkinter import * 
from item import *
from random import randint



class Room:
    """A room has a name and a filepath that points to a .gif image."""

    def __init__(self, name:str, imageFilepath:str) -> None:
        self.name = name
        self.image = imageFilepath
        self.exits = {} 
        self.items: list[Item] = []
        self.itemNames: list[str] = []    
        self.isKey = False
        self.final = False



    def addExit(self, label:str, room:'Room'): 
        self.exits[label] = room
    
    def addItem(self, item:Item):
        self.items.append(item) 
    
    def addItemNames(self):
        for item in self.items:
            self.itemNames.append(item.name)
        
    def addItemNameSingle(self, item:Item):
        self.itemNames.append(str(item))

    
    def __str__(self) -> str:
        result = f'You are in {self.name}\n'

        result += 'You see: '
        for item in self.itemNames:
            result += item + ', '
        result = result.rstrip(', ')
        result += '\n'

        result += 'Exits: '
        for exits in self.exits.keys():
            result += exits + ', '
        result = result.rstrip(', ')
        result += '\n'

        return result
       
        
def randomRoom(name:str) -> Room:
    r = Room(name, 'room1.jpg') 
    testVar = randint(1,100)
    if testVar > 80:
        r.addItem(chair)
    for _ in range(2):
        added = randint(1,5)
        if added == 1 and table not in r.items:
            r.addItem(table)
        elif added == 2 and rug not in r.items:
            r.addItem(rug)
        elif added == 3 and bookcase not in r.items:
            r.addItem(bookcase)
        elif added == 4 and debris not in r.items:
            r.addItem(debris)
        elif added == 5 and shelf not in r.items:
            r.addItem(shelf)
    r.addItemNames()
    return r



            

