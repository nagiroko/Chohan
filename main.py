import sys
import random


def roll(type):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    result = dice2 + dice1
    print(result)
    if result % 2 == 0 and type == "even":
        print("you win")
    elif result % 2 == 1 and type == "odd":
        print("you win")
    else:
        print("you lose")
def Quit():
    sys.exit()
