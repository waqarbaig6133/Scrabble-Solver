import nltk
nltk.download('words')
from nltk.corpus import words

words = words.words()
letters = input("What are the letters present: ")

available_words = []

for x in english_words:
  intersection = list(set(letters) & set(english_words))
  if len(intersection) == len(list(x)):
    available_words.append(x)
print(sorted(avaiable_words, key = len))
    

