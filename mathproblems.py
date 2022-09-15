
def square1(z: int):
    print("====================================")
    for x1 in range (0,1000):
        for x2 in range ( 0,x1):
            if (x1**2+x2**2)==z:
                print (f'{x1}**2+{x2}**2={x1**2}+{x2**2}={z}')
                
    print("====================================")

def square2(z:int):
    print("====================================")
    for x1 in range (0,1000):
        for x2 in range(0,x1):
            for x3 in range (0,x2):
                if (x1**2+x2**2+x3**2)==z:
                     print (f'{x1}**2+{x2}**2+{x3}**2={x1**2}+{x2**2}+{x3**2}={z}')
    print("====================================")

def adder(z:int, y:int):
    print("====================================")
    for x1 in range(0,100):
        for x2 in range(0,x1):
            if(x1+x2)==z:
                if (x1*x2)==y:
                    print(f'{x1}+{x2}={z} and {x1}*{x2}={y}')
    print("====================================")

square1(36482)
square2(125)
adder(16,55)

