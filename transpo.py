import unittest


tekst = input('Enter text to transpose: ')

class App:
    def simpleTransposition(self, tekst: str):
        self.tekst = tekst
        temp1 = tekst[0::2]
        temp2 = tekst[1::2]

        tekst = temp1+temp2
        return tekst



app = App()

print(app.simpleTransposition(tekst))