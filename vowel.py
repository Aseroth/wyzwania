word = input('Podaj słowo ( bez polskich znaków) do zbadania:')

word.lower()

def vowels(word: str):
    number = 0
    number += word.count('a')
    number+= word.count('o')
    number+=word.count('i')
    number+=word.count('e')

    return number


print(vowels(word))