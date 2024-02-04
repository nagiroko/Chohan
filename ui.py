from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from main import Oddroll
from main import Quit
from main import Evenroll
from main import Result
game = Tk()

game.geometry("700x350")

global L
L = Label(game, text= "Hi")
L.config(font=("Courier",14))
def update():
    print(Result)
    L = Label(game, text= Result)
    L.config(font=("Courier", 14))


ttk.Button(game,text="Odd",command=lambda: [Oddroll(),update()]).pack(pady=20)
ttk.Button(game,text="Even",command=Evenroll).pack(pady=40)
ttk.Button(game,text="Quit",command=Quit).pack(pady=60)
L.pack()
game.mainloop()