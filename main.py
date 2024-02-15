import sys
import random


Result = str("")
dice = str("")
die1 = 0
die2 = 0
def Oddroll():
    global  die1
    global  die2
    result = die2 + die1
    global dice
    dice = "You rolled a " + str(die1) + " and a " + str(die2)
    global Result
    if result % 2 == 1:
       Result = "you win"
    else:
       Result = "you lose"



def Evenroll():
    global  die1
    global  die2
    result = die2 + die1
    global dice
    dice = "You rolled a " + str(die1) + " and a " + str(die2)
    global Result
    if result % 2 == 0:
        Result = "you win"
    else:
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

Roll()
Evenroll()
Oddroll()
