from tkinter import *
from roomadventure import *
from random import seed,Random


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

    def randomFloor(self, seed_:int, c:Character, floorNum:int):
        gameSeed = Random(seed_)
        numRooms = gameSeed.randint(5,15) 

        # pre-set rooms
        s1 = Room('Starting Room')
        t1 = Treasure('Treasure Room', c, floorNum)
        t1.addItemNames()
        h1 = Shop('Shop') 
        h1.addItemNames()
        u1 = Room('unsued')
        b1 = Boss('Boss Room', floorNum) 
        b1.addItemNames()

        floor : list[Room] = []
        floor.append(s1)

        for i in range(numRooms):
            var = randomRoom(f'Room {i+1}') 
            floor.append(var)
        for i in range(len(floor)):
            if floor[i] == floor[-1]:
                break
            n = 0
            while n == 0:
                direction = gameSeed.randint(1,8) 
                if direction in [1,2] and 'north' not in floor[i].exitLocations:
                    floor[i].addExit('north', floor[i+1])
                    floor[i+1].addExit('south', floor[i])
                    n = 1
                elif direction in [3,4] and 'east' not in floor[i].exitLocations: 
                    floor[i].addExit('east', floor[i+1])
                    floor[i+1].addExit('west', floor[i])
                    n = 1
                elif direction in [5,6] and 'south' not in floor[i].exitLocations:
                    floor[i].addExit('south', floor[i+1]) 
                    floor[i+1].addExit('north', floor[i])
                    n = 1
                elif direction in [7,8] and 'west' not in floor[i].exitLocations: 
                    floor[i].addExit('west', floor[i+1])
                    floor[i+1].addExit('east', floor[i])
                    n = 1
        
        # add Key to floor
        k = gameSeed.randint(1,len(floor)-1)
        floor[k].isKey = True 
        
        # add Treasure room
        n1 = 0
        while n1 == 0:
            treasure = gameSeed.randint(1,len(floor)-1)
            tDirec = gameSeed.randint(1,4) 
            if tDirec == 1 and 'north' not in floor[treasure].exitLocations:
                floor[treasure].addExit('north', t1)
                t1.addExit('south', floor[treasure])
                n1 = 1
            elif tDirec == 2 and 'east' not in floor[treasure].exitLocations: 
                floor[treasure].addExit('east', t1)
                t1.addExit('west', floor[treasure])
                n1 = 1
            elif tDirec == 3 and 'south' not in floor[treasure].exitLocations:
                floor[treasure].addExit('south', t1) 
                t1.addExit('north', floor[treasure])
                n1 = 1
            elif tDirec == 4 and 'west' not in floor[treasure].exitLocations: 
                floor[treasure].addExit('west', t1)
                t1.addExit('east', floor[treasure])
                n1 = 1

        # add Shop 
        n1 = 0
        while n1 == 0:
            shop = gameSeed.randint(1,len(floor)-1)
            hDirec = gameSeed.randint(1,4) 
            if hDirec == 1 and 'north' not in floor[shop].exitLocations:
                floor[shop].addExit('north', h1)
                h1.addExit('south', floor[shop])
                n1 = 1
            elif hDirec == 2 and 'east' not in floor[shop].exitLocations: 
                floor[shop].addExit('east', h1)
                h1.addExit('west', floor[shop])
                n1 = 1
            elif hDirec == 3 and 'south' not in floor[shop].exitLocations:
                floor[shop].addExit('south', h1) 
                h1.addExit('north', floor[shop])
                n1 = 1
            elif hDirec == 4 and 'west' not in floor[shop].exitLocations: 
                floor[shop].addExit('west', h1)
                h1.addExit('east', floor[shop])
                n1 = 1

        # add Boss room
        n1 = 0
        while n1 == 0:
            bDirec = gameSeed.randint(1,4) 
            if bDirec == 1 and 'north' not in floor[-1].exitLocations:
                floor[-1].addExit('north', b1)
                b1.addExit('south', floor[-1])
                n1 = 1
            elif bDirec == 2 and 'east' not in floor[-1].exitLocations: 
                floor[-1].addExit('east', b1)
                b1.addExit('west', floor[-1])
                n1 = 1
            elif bDirec == 3 and 'south' not in floor[-1].exitLocations:
                floor[-1].addExit('south', b1) 
                b1.addExit('north', floor[-1])
                n1 = 1
            elif bDirec == 4 and 'west' not in floor[-1].exitLocations: 
                floor[-1].addExit('west', b1)
                b1.addExit('east', floor[-1])
                n1 = 1
        
        floor.append(t1)
        floor.append(h1) 
        floor.append(u1)
        floor.append(b1) 
        return s1, floor

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
        r1.addGrabs('key')
        r2.addGrabs('fire')
        r3.addGrabs('doug')
        r4.addGrabs('butter')

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

        if item in self.currentRoom.items:
            status = self.currentRoom.items[item]
        
        self.setStatus(status)


    def handleTake(self, grabs):
        status = Game.STATUS_BAD_GRABS

        if grabs in self.currentRoom.grabbables:
            self.inventory.append(self.currentRoom.grabbables[grabs])
            self.currentRoom.grabbables.remove(grabs)
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
