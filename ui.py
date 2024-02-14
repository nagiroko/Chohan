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
rolled = Label(game,text="sss")
rolled.pack(pady= 10)
result = Label(game,text= "dd")
result.pack()
roll = Button(game,text= "Roll",command= Quit)
roll.pack(side= TOP,pady = 50)


game.mainloop()