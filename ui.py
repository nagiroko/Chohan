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
result = Label(game,text="")
diceRolled = Label(game,text='',font=("times",30))

#Buttons
roll = Button(game,text= "Roll",command= lambda: [State(),Roll(),Results()])
quit = Button(game,text= "Quit",command= Quit)
evenroll = Button(game,text= "EvenRoll",command= lambda: [State(),Evenroll(),Results(),diceFaces()])
oddroll = Button(game,text= "OddRoll",command= lambda: [State(),Oddroll(),Results(),diceFaces()])

desc.pack()
result.pack(pady= 10)
diceRolled.pack(pady= 35)

roll.place(relx= 0.5,rely= 0.8,anchor= CENTER)
quit.place(relx= 0.5,rely= 0.65,anchor= CENTER)
evenroll.place(relx=0.4,rely= 0.9,anchor= CENTER)
oddroll.place(relx=0.6,rely= 0.9,anchor= CENTER)

evenroll.config(state= DISABLED)
oddroll.config(state= DISABLED)
def Results():
    from main import Result
    result.config(text=Result)
    diceRolled.config(text="")

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
def diceFaces():
    from main import die1
    from main import die2
    die1 -= 1
    die2 -= 1
    dice_dots = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    dice1 = dice_dots[die1]
    dice2 = dice_dots[die2]
    diceRolled.config(text='{}  {}'.format(dice1,dice2))


game.mainloop()