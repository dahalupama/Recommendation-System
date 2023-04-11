import pickle
import streamlit as st
import requests
import os

    


def recommend(Topic):
    index = Topics[Topics['Topic_Name'] == Topic].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_Topic_Names = []
    
    for i in distances[1:6]:
        # fetch the movie poster
        recommended_Topic_Names.append(Topics.iloc[i[0]].Topic_Name)

    return recommended_Topic_Names


st.header('Topic Recommender System')
Topics= pickle.load(open('Topics_list.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

Topics_list = Topics['Topic_Name'].values
selected_Topic = st.selectbox(
    "Type or select a Topics from the dropdown",
    Topics_list
)

if st.button('Show Recommendation'):
    recommended_Topic_Names= recommend(selected_Topic)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_Topic_Names[0])
        
    with col2:
        st.text(recommended_Topic_Names[1])
    

    with col3:
        st.text(recommended_Topic_Names[2])
        
    with col4:
        st.text(recommended_Topic_Names[3])
        
    with col5:
        st.text(recommended_Topic_Names[4])
        





