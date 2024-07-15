import nltk
nltk.download('words')
from nltk.corpus import words

words = words.words()
letters = input("What are the letters present: ")

present_words = []

for x in words:
  intersection = list(set(x) & set(words))
  if len(intersection) == len(x):
    present_words.append(x)
print(sorted(present_words, key = len))
    

