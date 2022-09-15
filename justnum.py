word = input('Podaj fraze mieszana ( słowa i liczby ): ')


def just_nums(word: str):
    nums = int(''.join(filter(str.isdigit, word)))

    return nums


print(just_nums(word))

