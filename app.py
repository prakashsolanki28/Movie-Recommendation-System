import streamlit as st
import pandas as pd
import pickle
import requests


def getPoster(movie_id):
    try:
        response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=7b4f65a7187be77199a7533d61481d7a&language=en-US'.format(movie_id))
        response = response.json()
        return "https://image.tmdb.org/t/p/w500"+response['poster_path']
    except:
        return "https://www.movienewz.com/img/films/poster-holder.jpg"        

def get_movie_recommendation(movie, movies_list, similarity):
    movie_index = movies_list[movies_list['title'] == movie].index[0]
    distance = similarity[movie_index]
    movies_list_with_indices = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:7]
    recommendations = []
    recommendations_poster = []
    for i in movies_list_with_indices:
        recommendations.append(movies_list.iloc[i[0]]['title'])
        recommendations_poster.append(getPoster(movies_list.iloc[i[0]]['movie_id']))
    return recommendations, recommendations_poster

movies_dict = pickle.load(open('movies.pkl','rb'))
movies_list = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))


st.title("Movie Recommender System")
selected_movies = st.selectbox('How would you like to be contacted?',movies_list['title'].values)

if st.button('Recommend', type="primary"):
    names, posters = get_movie_recommendation(selected_movies, movies_list, similarity)
    num_columns = 3
    num_rows = 3

    for i in range(num_rows):
        row_col1, row_col2, row_col3 = st.columns(num_columns)
        
        if i * num_columns < len(posters):
            with row_col1:
                st.image(posters[i * num_columns], width=200)
                st.text(names[i * num_columns])

        if i * num_columns + 1 < len(posters):
            with row_col2:
                st.image(posters[i * num_columns + 1], width=200)
                st.text(names[i * num_columns + 1])

        if i * num_columns + 2 < len(posters):
            with row_col3:
                st.image(posters[i * num_columns + 2], width=200)
                st.text(names[i * num_columns + 2])
