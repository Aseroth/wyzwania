class square():
    def __init__(self,*args):
        self.args = args

    def area(self):
        if len(self.args)==1:
            return self.args[0]*self.args[0]
        elif len(self.args)>1 and len(self.args)==2:
            return self.args[0]*self.args[1]

class rectangle(square):
    def __init__(self,*args) :
        self.args = args


kwadrat = square(5)
prostokat = rectangle(6,5)


print(kwadrat.area())
print(prostokat.area())

    
