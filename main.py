import nltk
nltk.download('words')
from nltk.corpus import words
from collections import Counter

# Load the list of English words
word_list = words.words()

# Get user input
letters = input("What are the letters present: ")

# Count the occurrences of each letter in the input
letters_count = Counter(letters)

# List to store words that can be made using the input letters
present_words = []

# Check which words can be formed using the input letters
for word in word_list:
    word_count = Counter(word)
    if all(word_count[char] <= letters_count[char] for char in word_count):
        present_words.append(word)

# Print the matching words



LETTER_SCORES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 
    'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 
    'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}
i = 0
score = 0
word_score = []
for x in present_words:
    score = 0
    for y in x:
        score+=LETTER_SCORES[y]
    word_score.append(score)

new = []
for x in present_words:
    new.append(f'{x}: {word_score[present_words.index(x)]}')
print(new)

    
