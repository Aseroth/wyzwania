to_check = input('Podaj ciag z xo lub bez: ')

to_check.lower()

def count_xo(xoxo:str):
    x_num = 0
    o_num = 0

    x_num += xoxo.count('x')
    o_num += xoxo.count('o')

    if x_num == o_num:
        return True
    elif x_num !=o_num:
        return False
    else:
        return True


print(count_xo(to_check))