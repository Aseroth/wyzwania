import random
from random import randint



def dice1():
    
    throws = 0
    dices = [randint(1,6), randint(1,6)]
    
    while sum(dices)!=12:
        dices[0]=randint(1,6)
        dices[1]=randint(1,6)
        throws+=1
    print(f'P1: {dices[0]}:{dices[1]} -> {throws}')
    return throws

def dice2():
    
    throws2 = 0
    dices = [randint(1,6), randint(1,6)]
    
    while sum(dices)!=12:
        dices[0]=randint(1,6)
        dices[1]=randint(1,6)
        throws2+=1
    print(f'P2: {dices[0]}:{dices[1]} -> {throws2}')
    
    return throws2


def main():
    x = dice1()
    y = dice2()
    if x > y:
        print(f'Player 1 lost  {x} against {y} ')
    elif x < y:
        print(f'Player 2 lost  {x} against {y} ')
    elif x == y:
        print(f'Draw {x} : {y}')

main()