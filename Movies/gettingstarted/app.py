from io import TextIOWrapper
import pandas as pd
from flask import Flask, request, render_template
#from utils import movies, lookup_title
#from recommender import recommend_random

app = Flask(__name__)
movies=pd.read_csv('movies.csv')
# this decorator gives our function new functionality
# it now knows in which URL to redener the information
@app.route('/')
def landing_page():
    '''
    this page takes in user info via a html form

    '''
    return render_template('landing_page.html')

from recommend_movie import recommend_movie
@app.route('/recommendations')
def recommender():
    
    movie_ids = request.args.getlist('movie_ids', type=int)
    
    ratings = request.args.getlist('ratings', type=int)

    query = dict(zip(movie_ids, ratings))

    top = recommend_movie(query=query)
 
    return render_template('recommendations.html', top=top)

@app.route('/movies/<int:movieId>')
def movie_info(movieId):
    '''
    this page give the user info about the movie
    '''
    info = movies.set_index('movieId').loc[movieId]
    # TODO: use the search_title function in the utils.py to find the movie from the dataset

    return render_template('movie_info.html', info=info, movieId=movieId)

if __name__ == "__main__":
    app.run(debug=True, port=5000)