

def to_bin_hex(integer: int, choice):
    if choice =='b':
        binary = "{0:b}".format(integer)
        return binary
    elif choice =='h':
        hexary = hex(integer)
        return hexary
    


print(to_bin_hex(19,'b'))
print(to_bin_hex(19,'h'))

