
calc = input('Wprowadz działanie matematyczne: ')


def calcul(*args):
    code = compile(*args, "<string>", "eval")
    print (*args,'=',eval(code))



calcul(calc)