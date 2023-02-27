imiona = ["bartek", "dominika", "tymoteusz", "łucja", "laura"]


for names in imiona:
    print(names)

#zadanie 1
for x in range(10):
    suma=0
    for y in range(x):
        suma+=y
    print(suma)


#zadanie 2
for i in range(1,10):
    print(i**3)


#while zadanie 1

x=0
sum=0
while x<=10:
    sum+=x
    print(sum)
    x+=1