import random 
from random import randint



checkNUm = randint(1,45)

myNum = None
count=0
while myNum !=checkNUm:
    myNum = int(input('Podaj liczbe z przedziały 1-45: '))

    if myNum> checkNUm:
        print('Podana liczba jest za duża')
    elif myNum < checkNUm:
        print('Podana liczba jest za mała')

    count+=1

    if myNum == checkNUm:
        break

print(f'Brawo udało ci się odgadnąć liczbę {checkNUm} za {count} razem')