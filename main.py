import sys
import random


Result = str("")
dice = str("")
def Oddroll():
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    result = die2 + die1
    global dice
    dice = "You rolled a " + str(die1) + " and a " + str(die2)
    global Result
    if result % 2 == 1:
       Result = "you win"
    else:
       Result = "you lose"

def Evenroll():
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    result = die2 + die1
    global dice
    dice = "You rolled a " + str(die1) + " and a " + str(die2)
    global Result
    if result % 2 == 0:
        Result = "you win"
    else:
        Result = "you lose"
def Quit():
    sys.exit()
