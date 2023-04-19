#######
# Names: Logan Coker, Bryce Mounts, Andrew Rupp
# desc: Imporved room adventrue thing
#######


from tkinter import *
from game import *
from end_screens import *

###
# Before you play:
#   For grading, we tested on seed 77 and everything works.
#   For that seed, the key is in room 8, so you don't have to 
#   search each and every room. 
###


seed = input('Seed: ')
window = Tk()
window.title('Room Adventure... RevOluTionS')
game = Game(window, seed)
game.play()
window.mainloop() 


