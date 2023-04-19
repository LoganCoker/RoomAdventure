


class Item:
    def __init__(self,name:str, desc:str, type_:'Item', isGrabbable:bool = False) -> None:
        self.name = name 
        self.description = desc
        self.type = type_
        self.grabbable = isGrabbable

    ###
    @property
    def name(self):
        return self._name 

    @property
    def description(self):
        return self._description 

    @property
    def type_(self):
        return self._type

    @property
    def grabbable(self):
        return self._grabbable 

    
    @name.setter
    def name(self, name:str):
        self._name = name
        

    @description.setter
    def description(self, desc:str):
        self._description = desc
        

    @type_.setter
    def type_(self, type_:'Item'):
        self._type = type_
        

    @grabbable.setter
    def grabbable(self, grab:bool):
        self._grabbable = grab
    ###

    def __str__(self) -> str:
        return self.name
    

class Usable(Item):
    def __init__(self, name: str, desc: str) -> None:
        super().__init__(name, desc, Usable, True)
        self.grabbable = True


class Enviornment(Item):
    def __init__(self, name: str, desc: str, isGrabbable: bool = False) -> None:
        super().__init__(name, desc, Enviornment, isGrabbable)



searchable = "There could be something in/around it."
grabbable = "This could be useful in the future."


###### Pre-Set Items ######
chair       = Item('chair', "A delapidated wooden chair. I don't think I should sit on it.", Enviornment)
table       = Enviornment('table', f'A broken wooden table. {searchable}')
rug         = Enviornment('rug', f'A rug with holes all across it. {searchable}') 
bookcase    = Enviornment('bookcase', f'It has a lot of tattered books on it. {searchable}')
debris      = Enviornment('debris', f'Looks like part of the ceiling collapsed. {searchable}')
shelf       = Enviornment('shelf', f'A broken wooden shelf, barley holding itself together. {searchable}')
painting    = Enviornment('painting', f'A colorful painting on the wall of a man standing in the middle of a vibrant room, the man has a weird neck tattoo alomost looking like the number 2. {searchable}')
puzzle      = Enviornment('puzzle', f'It looks like a childrens puzzle, it almost seems like it is in the shape of a key, I wonder what this could mean? {searchable}')

brick       = Usable('brick', f'A nearly destroyed brick, probably from the ceiling. {grabbable}')
book        = Usable('book', f"The title is faded, I can't make it out. {grabbable}")
leg         = Usable('chair leg', f'The leg of the chair I just crushed. Why did I sit on it... {grabbable}')
key         = Usable('key', f'A very rusted key. {grabbable}') 
note        = Usable('note', f'One of these three doors lead to victory, the other three will lead to your death. Choose wisely. {grabbable}')
sleg        = Usable('sleghammer', f'A heafty tool used for breaking things. {grabbable}') 
crois       = Usable('croissant', f'A noice warm, buttered croissant. How did it get here? {grabbable}')



allItemList     =   [chair, table, rug, bookcase, debris, shelf,
                    painting, puzzle, brick, book, leg, key, note, sleg, crois]


allItemsStrList =   ['chair', 'table', 'rug', 'bookcase', 'debris', 'shelf', 'painting', 'puzzle', 'brick', 'book', 
                    'chair leg', 'key', 'note', 'sleg', 'croissant'] 


