from unittest import result
import string
punc = string.punctuation
from collections import Counter

length= int(input("Length of the word that you are interested: "))

with open('pelekapasaka.txt', 'r', encoding='utf-8') as f:

    ff = f.read()
ff_list = ff.split()

empty = []

for item in ff_list:
    empty.append(item.strip(punc).lower())

words = []
clean = []
for i in empty:

    if length == len(i):
        words.append(i)
        if i not in clean:
            clean.append(i)
print(i)

word_count = dict(Counter(words))
print(word_count)

clean.sort()     
for j in clean:
    print(j)
    print(word_count[j])