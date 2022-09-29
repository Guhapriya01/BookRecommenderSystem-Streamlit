import pickle
import streamlit as st
import requests

def recommend(title):
    index = new_df[new_df['Title'] == title].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_book_names = []
    recommended_book_posters = []
    for i in distances[1:7]:
        books_id = new_df.iloc[i[0]].Path
        recommended_book_posters.append(books_id)
        recommended_book_names.append(new_df.iloc[i[0]].Title)

    return recommended_book_names,recommended_book_posters


st.header('Book Recommender System')
new_df = pickle.load(open('book_list.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

book_list = new_df['Title'].values
selected_book = st.selectbox(
    "Type or select a book from the dropdown",
    book_list
)

if st.button('Show Recommendation'):
    recommended_book_names,recommended_book_posters = recommend(selected_book)
    col1,col2,col3 = st.columns(3)
    with col1:
        st.text(recommended_book_names[0])
        st.image(recommended_book_posters[0])
    with col1:
        st.text(recommended_book_names[1])
        st.image(recommended_book_posters[1])

    with col2:
        st.text(recommended_book_names[2])
        st.image(recommended_book_posters[2])
    with col2:
        st.text(recommended_book_names[3])
        st.image(recommended_book_posters[3])
    with col3:
        st.text(recommended_book_names[4])
        st.image(recommended_book_posters[4])
    with col3:
        st.text(recommended_book_names[5])
        st.image(recommended_book_posters[5])
