from urllib.parse import MAX_CACHE_SIZE
import streamlit as st
from fast_autocomplete import AutoComplete
import NLP_Model
import pickle

with open('ListOfWords.pkl', 'rb') as f:
    ListOfWords = pickle.load(f)

ListOfWords = list(ListOfWords)

AvgLenght = 0

for i in ListOfWords:
    AvgLenght += len(i)

AvgLenght = AvgLenght / len(ListOfWords)

print(AvgLenght)


# print("The Total Lenght of the List is:",len(ListOfWords))

words = {}

for word in ListOfWords:
    words[word] = {}
        
# print(words)

st.title("Welcome to SmartDiet", anchor=None)
st.header("Please Do Enter your food item ", anchor=None)


autocomplete = AutoComplete(words=words)
max_cost = int(AvgLenght // 4)
max_size = int(AvgLenght // 4)
print(max_cost , max_size)




selected = st.text_input("")
KeyWords_Math = autocomplete.search(word=selected, max_cost=max_cost, size=max_size)
KeyWords_NLP = NLP_Model.my_autocorrect(selected)
NewKeyWords = []

for i in KeyWords_Math:
    NewKeyWords.append(str(i[0]))

st.selectbox("Search with AI - Math and Tree Data Structure",NewKeyWords, index=0)

KeyWords_NLP = NLP_Model.my_autocorrect(selected)

st.selectbox("Search with NLP Model" , KeyWords_NLP, index=0)
print(KeyWords_Math)