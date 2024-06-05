import streamlit as st
import json
from Classifier import KNearestNeighbours
from operator import itemgetter
import requests
from bs4 import BeautifulSoup
import urllib.parse

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

# Load data and movies list from corresponding JSON files
with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
with open('titles.json', 'r', encoding='utf-8') as f:
    movie_titles = json.load(f)

hdr = {'User-Agent': 'Mozilla/5.0'}

def movie_poster_fetcher(imdb_link):
    """Fetch and display the movie poster."""
    hdr = {'User-Agent': 'Mozilla/5.0'}
    # Send a GET request to the IMDb link
    response = requests.get(imdb_link, headers=hdr)
    
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find the movie poster element
    poster_elem = soup.find("meta", property="og:image")
    
    # Extract the URL of the movie poster
    if poster_elem:
        poster_url = poster_elem.get('content')
        return poster_url
    else:
        print("Movie poster not found on IMDb.")
        return None

def knn(test_point, k):
    # Create dummy target variable for the KNN Classifier
    target = [0 for _ in movie_titles]
    # Instantiate object for the Classifier
    model = KNearestNeighbours(data, target, test_point, k=k)
    # Run the algorithm
    model.fit()
    # Distances to most distant movie
    max_dist = sorted(model.distances, key=itemgetter(0))[-1]
    # Print list of recommendations
    table = []
    for i in model.indices:
        # Returns back movie title and imdb link
        table.append([movie_titles[i][0], movie_titles[i][2]])
    return table

if __name__ == '__main__':
    genres = ['Action', 'Adventure', 'Animation', 'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Family',
              'Fantasy', 'Film-Noir', 'Game-Show', 'History', 'Horror', 'Music', 'Musical', 'Mystery', 'News',
              'Reality-TV', 'Romance', 'Sci-Fi', 'Short', 'Sport', 'Thriller', 'War', 'Western']
    movies = [title[0] for title in movie_titles]
    st.header('Movie Recommender')
    apps = ['--Select--', 'Movie based', 'Criteria based']
    app_options = st.selectbox('Select application:', apps)
    if app_options == 'Movie based':
        movie_select = st.selectbox('Select movie:', ['--Select--'] + movies)
        if movie_select == '--Select--':
            st.write('Select a movie')
        else:
            n = st.number_input('Number of movies:', min_value=5, max_value=20, step=1)
            genres = data[movies.index(movie_select)]
            test_point = genres
            table = knn(test_point, n)
            num_columns = len(table)
            columns = st.columns(num_columns)
            for i, (movie, link) in enumerate(table):
                with columns[i]:
                    # Displays movie title with link to IMDb
                    st.markdown(f"[{movie}]({link})")
                    poster_url = movie_poster_fetcher(link)
                    if poster_url:
                        st.image(poster_url, caption=movie, use_column_width=False, width=140)
                    else:
                        st.write("No poster found for this movie.")

    elif app_options == apps[2]:
        options = st.multiselect('Select genres:', genres)
        if options:
            imdb_score = st.slider('IMDb score:', 1, 10, 8)
            n = st.number_input('Number of movies:', min_value=5, max_value=20, step=1)
            test_point = [1 if genre in options else 0 for genre in genres]
            test_point.append(imdb_score)
            table = knn(test_point, n)
            num_columns = len(table)
            columns = st.columns(num_columns)
            for i, (movie, link) in enumerate(table):
                with columns[i]:
                    # Displays movie title with link to IMDb
                    st.markdown(f"[{movie}]({link})")
                    poster_url = movie_poster_fetcher(link)
                    if poster_url:
                        st.image(poster_url, caption=movie, use_column_width=False, width=140)
                    else:
                        st.write("No poster found for this movie.")

        else:
            st.write("This is a simple Movie Recommender application. "
                     "You can select the genres and change the IMDb score.")
    else:
        st.write('Select option')
