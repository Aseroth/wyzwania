peaks = input('Podaj wysokości szczytów oddzielone spacją: ')



def gain_calc(*args):
    print(*args)
    x = args
    y = x.split(' ')
    print(*y)


gain_calc(peaks)