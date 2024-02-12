from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from main import Oddroll
from main import Quit
from main import Evenroll


game = Tk()

game.geometry("700x350")



desc = Label(game,text="Press odd or even button to bet on outcome")
desc.pack()


game.mainloop()