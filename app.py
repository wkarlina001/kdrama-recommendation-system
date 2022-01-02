import streamlit as st
import requests
import pickle
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from bing_image_downloader import downloader
import os

def fetch_poster(title):
    downloader.download("korean-"+title, limit=1, output_dir='image', \
        adult_filter_off=True, force_replace=False, timeout=60, verbose=True)
    return './image/korean-'+title

def make_recommendation(title):
    movie_index = movies[movies.Drama_Name == title]["index"].values[0]
    similar_movies = list(enumerate(similarity[movie_index])) #accessing the row corresponding to given movie to find all the 

    sorted_similar_movies = sorted(similar_movies,key=lambda x:x[1],reverse=True)[1:5]
    similar_movies = []
    movies_poster = []
    ratings = []
    for element in sorted_similar_movies:
        title = movies[movies.index == element[0]]["Drama_Name"].values[0]
        similar_movies.append(title)
        
        try:
            os.listdir('./image/korean-'+title)
        except:
            fetch_poster(title)
        
        image = os.listdir('./image/korean-'+title)[0]
        movies_poster.append('./image/korean-'+title+'/'+image)
        ratings.append(movies[movies.index == element[0]]["Rating(Out of 10)"].values[0])

    return similar_movies,movies_poster,ratings

movies = pickle.load(open('./movie_list.pkl','rb'))
similarity = pickle.load(open('./similarity.pkl','rb'))

st.markdown("<h1 style='text-align: center; color: black;'>K-Drama Recommender System</h1>", unsafe_allow_html=True)
movie_list = sorted(movies['Drama_Name'].values)
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters,ratings = make_recommendation(selected_movie)
    col1, col2 = st.columns(2)
    with col1:
        st.text(recommended_movie_names[0]+" - Rating : "+str(ratings[0]))
        st.image(recommended_movie_posters[0], width=350)
    with col2:
        st.text(recommended_movie_names[1]+" - Rating : "+str(ratings[1]))
        st.image(recommended_movie_posters[1], width=350)

    col3, col4= st.columns(2)
    with col3:
        st.text(recommended_movie_names[2]+" - Rating : "+str(ratings[2]))
        st.image(recommended_movie_posters[2], width=350)
    with col4:
        st.text(recommended_movie_names[3]+" - Rating : "+str(ratings[3]))
        st.image(recommended_movie_posters[3], width=350)
