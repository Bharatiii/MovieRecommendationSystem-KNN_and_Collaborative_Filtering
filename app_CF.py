
import pickle
import streamlit as st
import requests
from operator import itemgetter
import base64

st.markdown(
    """
<style>

.stApp {
background-image: url("https://pointerclicker.com/wp-content/uploads/2022/12/A-TV-with-bias-lighting-behind-960x960.jpg");
background-size: cover;
}
.reportview-container .markdown-text-container {
    font-family: monospace;
    
    
    background-size: cover;
    {
    background-color: rgba(0, 0, 0, 0);
    }
}
.stHeader {
    background-color: rgba(0, 0, 0, 0);
}
.sidebar .sidebar-content {
    background-image: linear-gradient(#2e7bcf,#2e7bcf);
    color: white;
}
.Widget>label {
    color: white;
    font-family: monospace;
}
[class^="st-b"]  {
    color: white;
    font-family: monospace;
}
.st-bb {
    background-color: transparent;
}
.st-at {
    background-color: #38ACEC;
}
footer {
    font-family: monospace;
}
.reportview-container .main footer, .reportview-container .main footer a {
    color: #38ACEC;
}

</style>
""",
    unsafe_allow_html=True,
)

def fetch_poster(id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=68fbbdeb2681f7f203e8f83109bb7551".format(id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend_title(movie):
    index=[]
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity1[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        id = movies.iloc[i[0]].id
        recommended_movie_posters.append(fetch_poster(id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters
def recommend_year(release_date):
    index=[]
    index = movies[movies['release_date'] == release_date].index[0]
    distances = sorted(list(enumerate(similarity2[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        id = movies.iloc[i[0]].id
        recommended_movie_posters.append(fetch_poster(id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters


st.header('Movie Recommender System Using Machine Learning')
movies = pickle.load(open('data/movie_list.pkl','rb'))
similarity1 = pickle.load(open('data/similarity1.pkl','rb'))
similarity2 = pickle.load(open('data/similarity2.pkl','rb'))


apps = ['--Select--', 'Movie based', 'Year based']
app_options = st.selectbox('Select application:', apps)
if app_options == 'Movie based':
    movie_list = movies['title'].values
    selected_movie = st.selectbox(
        "Type or select a movie from the dropdown",
        movie_list
    )

    if st.button('Show Recommendation'):
        recommended_movie_names,recommended_movie_posters = recommend_title(selected_movie)
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.image(recommended_movie_posters[0])
            st.text(recommended_movie_names[0])
        with col2:
            st.image(recommended_movie_posters[1])
            st.text(recommended_movie_names[1])

        with col3:
            st.image(recommended_movie_posters[2])
            st.text(recommended_movie_names[2])
        with col4:
            st.image(recommended_movie_posters[3])
            st.text(recommended_movie_names[3])
        with col5:
            st.image(recommended_movie_posters[4])
            st.text(recommended_movie_names[4])
elif app_options == 'Year based':
    movie_list = movies['release_date'].values
    selected_movie = st.selectbox(
        "Type or select a Year from the dropdown",
        movie_list
    )

    if st.button('Show Recommendation'):
        recommended_movie_names,recommended_movie_posters = recommend_year(selected_movie)
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.image(recommended_movie_posters[0])
            st.text(recommended_movie_names[0])
        with col2:
            st.image(recommended_movie_posters[1])
            st.text(recommended_movie_names[1])

        with col3:
            st.image(recommended_movie_posters[2])
            st.text(recommended_movie_names[2])
        with col4:
            st.image(recommended_movie_posters[3])
            st.text(recommended_movie_names[3])
        with col5:
            st.image(recommended_movie_posters[4])
            st.text(recommended_movie_names[4])
