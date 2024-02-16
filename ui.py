from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from main import Oddroll
from main import Quit
from main import Evenroll
from main import Roll


game = Tk()

game.geometry("700x350")


#labels
desc = Label(game,text="Press odd or even button to bet on outcome")
rolled = Label(game,text="")
result = Label(game,text="")

#Buttons
roll = Button(game,text= "Roll",command= lambda: [State(),Roll(),Results()])
quit = Button(game,text= "Quit",command= Quit)
evenroll = Button(game,text= "EvenRoll",command= lambda: [State(),Evenroll(),Results()])
oddroll = Button(game,text= "OddRoll",command= lambda: [State(),Oddroll(),Results()])

desc.pack()
rolled.pack(pady= 10)
result.pack()

roll.place(relx= 0.5,rely= 0.3,anchor= CENTER)
quit.place(relx= 0.5,rely= 0.5,anchor= CENTER)
evenroll.place(relx=0.4,rely= 0.9,anchor= CENTER)
oddroll.place(relx=0.6,rely= 0.9,anchor= CENTER)

evenroll.config(state= DISABLED)
oddroll.config(state= DISABLED)
def Results():
    from main import dice
    from main import Result
    rolled.config(text=dice)
    result.config(text=Result)

state = 0
def State():
    global state
    if state == 0:
        evenroll.config(state=ACTIVE)
        oddroll.config(state=ACTIVE)
        roll.config(state=DISABLED)
        state = 1
    else:
        evenroll.config(state=DISABLED)
        oddroll.config(state=DISABLED)
        roll.config(state=ACTIVE)
        state = 0


game.mainloop()