
k=int(input())

def expanded_form(k):
    
    result = []
    for index, digit in enumerate(str(k)[::-1]):
        if int(digit)!=0:
            result.append(digit+('0'*index))

    return ' + '.join(result[::-1])


print(expanded_form(k))