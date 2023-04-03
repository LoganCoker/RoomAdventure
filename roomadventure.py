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
        


class Game:
    pass
    

