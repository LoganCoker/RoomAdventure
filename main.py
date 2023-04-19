#######
# Names: Logan Coker, Bryce Mounts
# Names: Logan Coker, Andrew Rupp
# desc: Imporved room adventrue thing
#######


from tkinter import *
from game import *
from end_screens import *


seed = input('Seed: ')
window = Tk()
window.title('Room Adventure... RevOluTionS')
game = Game(window, seed)
game.play()
window.mainloop() 
<<<<<<< HEAD


=======
>>>>>>> fc3dc573aad22a8db79c21d369495107dec85388
