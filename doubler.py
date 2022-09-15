word = input('Podaj słowo: ')


def doubler(word: str):
    doubled = ''

    for x in range( len(word)):
        doubled+=word[x]*2

    print(doubled)



doubler(word)