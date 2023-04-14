from tkinter import *
from game import *




window = Tk()
window.title('Room Adventure... RevOluTionS')
game = Game(window)
game.play()
window.mainloop()