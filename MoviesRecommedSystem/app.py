import streamlit as st
import pickle
import pandas as pd
import requests
import os

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?append_to_response=Batman%20Returns&language=en-US"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJiODU4Y2Q5OTFmNjcwMTBlMmRhMDgzNDIyN2UyYTIyZSIsIm5iZiI6MTczMjI3OTQ5Ny4wMjk2NzEsInN1YiI6IjY3NDA3NTZjY2NlNjZjZjg5OWU5MmY1YiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.6bqp-i3EJnJ_j24pdOD0klwoDlSTdjvBU9bkeWYQuog"
    }
    try:
        response = requests.get(url, headers=headers, timeout=1)  # Set timeout to 10 seconds
        #response.raise_for_status()
        data = response.json()
        #st.write(data)
        poster_path = data.get('poster_path')
        if poster_path:
            full_path = f"https://image.tmdb.org/t/p/w500/{poster_path}"
            return full_path
        else:
            return "https://via.placeholder.com/500"
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching poster: {e}")
        return "https://via.placeholder.com/500"

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = similarity[index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].id
        recommended_movie_names.append(movies.iloc[i[0]].title)
        #recommended_movie_posters.append(fetch_poster(movie_id))
    return recommended_movie_names #, recommended_movie_posters

st.title("Movie Recommender System")
movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Recommend'):
    names = recommend(selected_movie)
    cols = st.columns(5)
    for col, name in zip(cols, names, ):
        col.text(name)
      #  col.image(poster)
