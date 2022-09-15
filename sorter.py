from audioop import reverse
import random
from random import randint

to_sort = []

for x in range(10):
    to_sort.append(randint(0,20))

print(to_sort)

def sorting(lista, sorter=None):
    if sorter =='asc':
        return sorted(lista)
    elif sorter =='desc':
        return sorted(lista, reverse=True)
    elif sorter == None:
        return lista

print(sorting(to_sort, 'asc'))
print(sorting(to_sort, 'desc'))
print(sorting(to_sort))