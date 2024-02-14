from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from main import Oddroll
from main import Quit
from main import Evenroll
from main import Roll


game = Tk()

game.geometry("700x350")



desc = Label(game,text="Press odd or even button to bet on outcome")
rolled = Label(game,text="sss")
result = Label(game,text= "dd")

roll = Button(game,text= "Roll",command= Roll)
quit = Button(game,text= "Quit",command= Quit)
evenroll = Button(game,text= "EvenRoll",command= Evenroll)
oddroll = Button(game,text= "OddRoll",command= Oddroll)

desc.pack()
rolled.pack(pady= 10)
result.pack()

roll.place(relx= 0.4,rely= 0.4,anchor= CENTER)
quit.place(relx= 0.6,rely= 0.4,anchor= CENTER)
evenroll.place(relx=0.4,rely= 0.7,anchor= CENTER)
oddroll.place(relx=0.6,rely= 0.7,anchor= CENTER)

game.mainloop()