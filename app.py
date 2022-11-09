import streamlit as st
import model



@st.cache(suppress_st_warning=True)
def main(selected):

    KeyWords_Math = model.autocomplete.search(word=selected, max_cost=3, size=10)
    NewKeyWords = []
    for i in KeyWords_Math:
        NewKeyWords.append(str(i[0]))
    

    st.selectbox("Search with AI - Math and Tree Data Structure",NewKeyWords, index=0)

if __name__ == "__main__":
    st.title("Welcome to SmartDiet", anchor=None)
    st.header("Please Do Enter your food item ", anchor=None)
    selected = st.text_input("")
    main(selected)
