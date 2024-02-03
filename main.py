import sys
import random


def Oddroll():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    result = dice2 + dice1
    print(result)
    if result % 2 == 1:
        print("you win")
    else:
        print("you lose")

def Evenroll():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    result = dice2 + dice1
    print(result)
    if result % 2 == 0:
        print("you win")
    else:
        print("you lose")
def Quit():
    sys.exit()
