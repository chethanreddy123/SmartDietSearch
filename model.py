
import pickle
with open('ListOfWords.pkl', 'rb') as f:
    ListOfWords = pickle.load(f)

ListOfWords = list(ListOfWords)

AvgLenght = 0
for i in ListOfWords:
    AvgLenght += len(i)

AvgLenght = AvgLenght / len(ListOfWords)

words = {}

for word in ListOfWords:
    words[word] = {}

# print(AvgLenght)
from fast_autocomplete import AutoComplete
autocomplete = AutoComplete(words=words)