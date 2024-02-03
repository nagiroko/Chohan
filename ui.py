from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from main import Oddroll
from main import Quit
from main import Evenroll
game = Tk()

game.geometry("700x350")


ttk.Button(game,text="Odd",command=Oddroll).pack(pady=20)
ttk.Button(game,text="Even",command=Evenroll).pack(pady=40)
ttk.Button(game,text="Quit",command=Quit).pack(pady=60)
game.mainloop()