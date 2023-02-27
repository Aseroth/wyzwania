import random

slowa = ['stół', 'marchewka', 'telewizor', 'telefon', 'burak', 'samochód', 'samolot']

word = random.choice(slowa)
wordcheck = word
word = list(word)
print(word, wordcheck)
random.shuffle(word)
result = ''.join(word)
print(result)