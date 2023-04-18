from tkinter import *
from roomadventure import *
from random import Random
from end_screens import *

croissantLimit = 0

lose = False



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
    STATUS_BAD_SEARCH = 'There is nothing there'
    STATUS_BAD_EAT = 'Are you insane?! You can\'t eat that!'

    WIDTH = 800
    HEIGHT = 600

    def __init__(self, parent, seed_: int) -> None:
        self.inventory = []
        Frame.__init__(self, parent)
        self.pack(fill=BOTH, expand=1)
        self.seed = seed_
    
    ###
    @property
    def seed(self):
        return self._seed


    @seed.setter
    def seed(self, seed_:int):
        self._seed = seed_
    ###


    def randomFloor(self, seed_:int):
        gameSeed = Random(seed_)
        numRooms = gameSeed.randint(5,15) 

        # pre-set rooms
        s1 = Room('Starting Room', 'room2.gif')

        s2 = Room('Secret Room', 'room3.gif')

        s2.addExit('door1', None)
        s2.addExit('door2', 'Escape')
        s2.addExit('door3', None)
        s2.addItem(note)


        floor : list[Room] = []
        floor.append(s1)

        for i in range(numRooms):
            var = randomRoom(f'Room {i+1}') 
            floor.append(var)
        for i in range(len(floor)):
            if floor[i] == floor[-1]:
                floor[i].addExit('down', n1)
                break
            n = 0
            while n == 0:
                direction = gameSeed.randint(1,8) 
                if direction in [1,2] and 'north' not in floor[i].exits:
                    floor[i].addExit('north', floor[i+1])
                    floor[i+1].addExit('south', floor[i])
                    n = 1
                elif direction in [3,4] and 'east' not in floor[i].exits: 
                    floor[i].addExit('east', floor[i+1])
                    floor[i+1].addExit('west', floor[i])
                    n = 1
                elif direction in [5,6] and 'south' not in floor[i].exits:
                    floor[i].addExit('south', floor[i+1]) 
                    floor[i+1].addExit('north', floor[i])
                    n = 1
                elif direction in [7,8] and 'west' not in floor[i].exits: 
                    floor[i].addExit('west', floor[i+1])
                    floor[i+1].addExit('east', floor[i])
                    n = 1
        
        n1 = 0
        while n1 == 0:
            secret = gameSeed.randint(1,len(floor)-1)
            tDirec = gameSeed.randint(1,4) 
            if tDirec == 1 and 'north' not in floor[secret].exits:
                floor[secret].addExit('north', s2)
                s2.addExit('door1', floor[secret])
                n1 = 1
            elif tDirec == 2 and 'east' not in floor[secret].exits: 
                floor[secret].addExit('east', s2)
                s2.addExit('door2', floor[secret])
                n1 = 1
            elif tDirec == 3 and 'south' not in floor[secret].exits:
                floor[secret].addExit('south', s2) 
                s2.addExit('north', floor[secret])
                n1 = 1
            elif tDirec == 4 and 'west' not in floor[secret].exits: 
                floor[secret].addExit('west', s2)
                s2.addExit('door3', floor[secret])
                n1 = 1

        # add Key to floor
        k = gameSeed.randint(1,len(floor)-1)
        floor[k].isKey = True 
        
        return s1


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


    def handleLook(self, item):
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


    def handleSearch(self, item):
        status = Game.STATUS_BAD_SEARCH

        if self.currentRoom.isKey:
            self.inventory.append(str(key))
            status = "Key acquired"

        elif item in allItemsStrList and item in self.currentRoom.itemNames:
            index = allItemsStrList.index(item)
            iteM:Item = allItemList[index]
            if iteM == bookcase:
                self.inventory.append(str(book))
                status = "Book acquired"
            elif iteM == rug:
                self.inventory.append(str(brick))
                status = "Brick acquired"
            elif iteM == table:
                self.inventory.append(str(crois))
                status = "Croissant acquired"
            elif iteM == debris:
                self.inventory.append(str(brick))
                status = "Book acquired"
            elif iteM == shelf:
                self.inventory.append(str(book))
                status = "Book acquired"
        self.setStatus(status)


    def handleEat(self, item):
        status = Game.STATUS_BAD_EAT

        if item in allItemsStrList and item in self.inventory:
            index = allItemsStrList.index(item)
            iteM:Item = allItemList[index]

            if iteM == crois:
                if croissantLimit == 1:
                    status = 'Bro! That croissant was so good! I will never be satsified with any other food from now on. What is even the point!?!?'
                    croissantLimit += 1
                if croissantLimit == 2:
                    status = 'That was dissapointing.'
                    croissantLimit += 1
                if croissantLimit == 3:
                    status = 'Why?'
                    croissantLimit += 1
                if croissantLimit == 4:
                    status = 'You couldn\'t take the thought of food any longer.'
                    self.kill()            

            if iteM == key:
                self.kill()
            
            if iteM == brick:
                status = "Oww! I bwoke my teef. I should wait until the next room to eat more."
        
        self.setStatus(status)


    def play(self):
        self.currentRoom = self.randomFloor(self.seed)
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
            
            case 'search':
                self.handleSearch(item=noun)

