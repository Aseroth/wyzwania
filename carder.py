cc_number = input('Podaj numer karty kredytowej:')


def hideit(card):
    to_print = '*'*(len(card)-4) + card[-4:]

    return to_print


print(hideit(cc_number))


    