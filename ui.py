from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from main import Oddroll
from main import Quit
from main import Evenroll


game = Tk()

game.geometry("700x350")



def update():
    from main import Result
    from main import dice
    action.set(dice)
    result.set(Result)

result = StringVar()
result.set("")
action = StringVar()
action.set("")
L = Label(game, textvariable = result)
desc = Label(game,text="Press odd or even button to bet on outcome")
desc.pack(pady= 2)
Action = Label(game, textvariable= action)
Action.pack(pady= 10)
L.pack(pady= 10)
ttk.Button(game,text="Odd",command=lambda: [Oddroll(),update()]).pack(side= LEFT )
ttk.Button(game,text="Even",command=lambda: [Evenroll(),update()]).pack(side= LEFT)
ttk.Button(game,text="Quit",command=Quit).pack(side= BOTTOM)

game.mainloop()