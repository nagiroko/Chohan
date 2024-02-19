import sys
import random


Result = str("")
dice = str("")
die1 = 0
die2 = 0
PlayerWins = 0
DealerWins = 0
def Oddroll():
    global  die1
    global  die2
    global PlayerWins
    global DealerWins
    result = die2 + die1
    global dice
    dice = "You rolled a " + str(die1) + " and a " + str(die2)
    global Result
    if result % 2 == 1:
       PlayerWins += 1
       Result = "you win"
    else:
       DealerWins += 1
       Result = "you lose"



def Evenroll():
    global  die1
    global  die2
    global PlayerWins
    global DealerWins
    result = die2 + die1
    global dice
    dice = "You rolled a " + str(die1) + " and a " + str(die2)
    global Result
    if result % 2 == 0:
        PlayerWins += 1
        Result = "you win"
    else:
        DealerWins += 1
        Result = "you lose"


def Roll():
    global  die1
    global  die2
    global dice
    global Result
    dice = ""
    Result = ""
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)

def Quit():
    sys.exit()

