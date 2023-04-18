#######
# Names: Logan Coker
# desc: Imporved room adventrue thing
#######


from tkinter import *
from game import *




window = Tk()
window.title('Room Adventure... RevOluTionS')
game = Game(window,77)
game.play()
window.mainloop()