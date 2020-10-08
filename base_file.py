import random

file = open('list_words.txt', 'r')

lines = file.readlines()
 
print('Generating random word... ')
print(lines[random.randint(0, len(lines)-1)])