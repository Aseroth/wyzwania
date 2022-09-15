from math import factorial



class App:
    def Pascal(self, n):
        self.n = n
        for i in range (self.n):
            for j in range(i+1):
                print(factorial(i)//(factorial(j)*factorial(i-j)), end=' ')

app = App()
app.Pascal(5)