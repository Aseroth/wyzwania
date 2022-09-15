frac1 = input('Podaj pierwszy ułamek (x/z): ')
frac2 = input('Podaj drugi ułamek (x/z): ')


def comparing(frac1, frac2):
    fraction1 = frac1.split('/')
    fraction2 = frac2.split('/')

    multi1 = int(fraction1[0]) * int(fraction2[1])
    multi2 = int(fraction1[1]) * int(fraction2[0])

    if multi1 > multi2:
        print(f'{frac1} jest wieksze od {frac2}')
    elif multi1 < multi2:
        print(f'{frac1} jest mniejsze od {frac2}')
    elif multi1 == multi2:
        print(f'{frac1} jest równe {frac2}')


comparing(frac1, frac2)