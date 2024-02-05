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
    print(Result)
    action.set(Result)

action = StringVar()
action.set("")
L = Label(game, textvariable = action)
ttk.Button(game,text="Odd",command=lambda: [Oddroll(),update()]).pack(pady=20)
ttk.Button(game,text="Even",command=lambda: [Evenroll(),update()]).pack(pady=40)
ttk.Button(game,text="Quit",command=Quit).pack(pady=60)
L.pack()
game.mainloop()