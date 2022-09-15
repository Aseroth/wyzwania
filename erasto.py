

zakres = int(input('Enter max number to check for prime numbers: '))
test_list = []

prime_list = [x*10 for x in range(5,9)]

print(prime_list)

def Primer():
    
    prime_list.append(min(test_list))
    for x in test_list:
        if x%(min(test_list))==0:
            test_list.remove(min(test_list))
            prime_list.append(min(test_list))

    print(test_list)



Primer()