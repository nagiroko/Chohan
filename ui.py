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
desc = Label(game,text="Press roll to start")
result = Label(game,text="")
total = Label(game,text= "")
diceRolled = Label(game,text='',font=("times",30))

#Buttons
roll = Button(game,text= "Roll",command= lambda: [State(),Roll(),Results()])
quit = Button(game,text= "Quit",command= Quit)
evenroll = Button(game,text= "EvenRoll",command= lambda: [Evenroll(),State(),Results(),diceFaces()])
oddroll = Button(game,text= "OddRoll",command= lambda: [Oddroll(),State(),Results(),diceFaces()])

desc.pack()
result.pack(pady= 10)
total.pack()
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
    diceRolled.config(text='{}  {}'.format("\u25FB", "\u25FB"))

state = 0
def State():
    global state
    from main import PlayerWins
    from main import DealerWins
    if state == 0:
        evenroll.config(state=ACTIVE)
        oddroll.config(state=ACTIVE)
        roll.config(state=DISABLED)
        desc.config(text="Press either odd or even to bet on the dice's value")
        total.config(text="")
        state = 1
    else:
        evenroll.config(state=DISABLED)
        oddroll.config(state=DISABLED)
        roll.config(state=ACTIVE)
        desc.config(text="Press roll to play again")
        total.config(text = 'Player {}:{} Dealer'.format(PlayerWins,DealerWins))
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