slownik = {"kawa": "czarna", "herbata":"oolong", "cukier":"trzcinowy"}

print(slownik.keys())
print(slownik.values())

for keys, values in slownik.items():
    print(f'{keys}:{values}')