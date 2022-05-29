from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
import ast
import re
from wsgiref.util import request_uri
from flask import Flask, redirect, render_template, request, redirect
import numpy as np
import pandas as pd
import os
from array import *
import requests

# read the file from the datset
credits = pd.read_csv("tmdb_5000_credits.csv")
movies = pd.read_csv("tmdb_5000_movies.csv")
movies = movies.merge(credits, on='title')  # merging the two datasets on coloum 'title'

#getting the the coloums to be used for getting similarity
movies = movies[['movie_id', 'title', 'overview',
                 'genres', 'keywords', 'cast', 'crew']]

# the data in this dataset is in the form of list
# function to get the value name
def convert(text):
    L = []
    for i in ast.literal_eval(text):
        L.append(i['name'])
    return L

movies['genres'] = movies['genres'].apply(convert)
movies['keywords'] = movies['keywords'].apply(convert)
movies['cast'] = movies['cast'].apply(convert)


movies['cast'] = movies['cast'].apply(lambda x: x[0:3]) # getting the top cast from all

# function to fetch the director from the crew list
def fetch_director(text):
    L = []
    for i in ast.literal_eval(text):
        if i['job'] == 'Director':
            L.append(i['name'])
    return L


movies['crew'] = movies['crew'].apply(fetch_director)

# getting of the space between the single name to avoid confusion in similarity
def collapse(L):
    L1 = []
    for i in L:
        L1.append(i.replace(" ", ""))
    return L1


movies['cast'] = movies['cast'].apply(collapse)
movies['crew'] = movies['crew'].apply(collapse)
movies['genres'] = movies['genres'].apply(collapse)
movies['keywords'] = movies['keywords'].apply(collapse)

# merge all the features we use in cosine similarity
movies['tags'] = movies['genres'] + movies['keywords'] + movies['cast'] + movies['crew']
new = movies.drop(columns=['genres', 'keywords', 'cast', 'crew'])


new['tags'] = new['tags'].apply(lambda x: " ".join(x))
new['tags'] = new['title']+ " " +new['tags']  # also joining title to get more similarity for serial movie parts

# assuming the maximum different features of all movies we are taking as 5000 (not more not less)
cv = CountVectorizer(max_features=5000, stop_words='english') 

vector = cv.fit_transform(new['tags']).toarray() #converting every movie's features into vector of 5000 dimensions 


#applying cosine similarity to the vectors
similarity = cosine_similarity(vector) 

# fetching movie posters from the movi_id 

def fetch_poster(movie_id):
    response = requests.get(
        'https://api.themoviedb.org/3/movie/{}?api_key=3779767ece38669f301aa9429abd03a1&append_to_response=credits'.format(movie_id))
    data = response.json()
    
    try:
        if str(data['poster_path']) == 'None':
            pass
        else: 
            return 'http://image.tmdb.org/t/p/w500/' + str(data['poster_path'])
    except:
        pass

#fetching movie details from the movie_id

def fetch_moviedetails(movie_id):
    response = requests.get(
        'https://api.themoviedb.org/3/movie/{}?api_key=3779767ece38669f301aa9429abd03a1&append_to_response=credits'.format(movie_id))
    data = response.json()
    movie_genre = ", ".join([genre["name"] for genre in data["genres"]])
    overview = data['overview']
    date = data['release_date']
    runtime = data['runtime']
    rating = data['vote_average']
    return movie_genre, overview, date, runtime, rating


# recommending movies based on cosine similarity index

def recommend(movie):
    index = new[new['title'].str.casefold() == movie.casefold()].index[0]
    searched = []
    # getting the movie we searched for (searched movie)
    search_movieId = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])[0:1] 
    for i in search_movieId:
        searched.append(new.iloc[i[0]].movie_id)
    s = searched[0]

    # list of recommended movies based on cosine similarity (sorted in descending order) 
    movie_list = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])[1:26] # getting top 25 movies (this step takes time since it hase to fetch movies from the API: more movies-->more time)
    
    recommended = []
    for i in movie_list:
        movie_id = new.iloc[i[0]].movie_id
        if fetch_poster(movie_id) != None:
            recommended.append((fetch_poster(movie_id), new.iloc[i[0]].title))

    return recommended, s


app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        try:
            content = request.form['content']
            result, id = recommend(content)
            search_poster = fetch_poster(id)
            search_genre, search_overview, search_date, search_runtime, search_rating = fetch_moviedetails(id)
            return render_template('test.html', content=content, result=result, search_poster=search_poster, search_genre=search_genre, search_overview=search_overview, search_date=search_date, search_runtime=search_runtime, search_rating=search_rating)
        except:
            return 'The movie you requested is not in our dataframe...... Please go back and check the spelling or try with some other movies :)'
    else:
        return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)
