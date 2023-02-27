

def silnia(n):
    if n>1:
        return n*silnia(n-1)
    return 

def silnia2(n):
    s=1
    for i in range(2, n+1):
        s*=i
    return s

silnia_in = int(input('Podaj liczbe do wyznaczenia silni: '))

#print(silnia(silnia_in))
print(silnia2(silnia_in))