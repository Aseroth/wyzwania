price = int(input('Podaj cene produktu: '))
disc = int(input('Podaj procent obniżki: '))


def calcul ( price: int, disc: int):
    final_price = price - (price * disc/100)

    return final_price



print (calcul(price, disc))