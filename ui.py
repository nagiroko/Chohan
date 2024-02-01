from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from main import roll
from main import Quit
game = Tk()

game.geometry("700x350")


ttk.Button(game,text="Odd",command=roll("odd")).pack(pady=20)
ttk.Button(game,text="Quit",command=Quit).pack(pady=40)
game.mainloop()