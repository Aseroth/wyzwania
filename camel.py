


class App:

    def solve(self, s):
        self.s = s
        tempIndex = ''
        bigIndex=''
        for letter in s:
            if letter.isalpha()==True:
                tempIndex+=(letter)

        for alpha in tempIndex:
            if alpha.isupper()==False:
                bigIndex+=alpha
            elif alpha.isupper()==True:
                bigIndex+=''
                bigIndex+=alpha
        
        return bigIndex
app = App()


print(app.solve('someNiceCamelCaseName'))

