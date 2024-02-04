import sys
import random

global Result
Result = str("sup")
def Oddroll():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    result = dice2 + dice1
    print(result)
    if result % 2 == 1:
       Result = "you win"
    else:
       Result = "you lose"

def Evenroll():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    result = dice2 + dice1
    print(result)
    if result % 2 == 0:
        Result = "you win"
    else:
        Result = "you lose"
def Quit():
    sys.exit()
