import random
from googlesearch import search

file = open('list_words.txt', 'r')
words = file.readlines()

lines = file.readlines()
print('Generating random word... ')
word = lines[random.randint(0, len(lines)-1)]
print(word)
print('You can find the meaning at ')
for i in search(word, tld='com', num=1, start=0, stop=10, pause=2.0):
    print(i)

print('Thank you :)')
