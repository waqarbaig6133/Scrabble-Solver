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

#Sorting process for highest score to lowest
LETTER_SCORES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 
    'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 
    'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}
scores = []
for x in present_words:
    a= [LETTER_SCORES[y] for y in x]
    scores.append(sum(a))
    

