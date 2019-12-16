from .models import db, Director, Movies
import pandas as pd

MOVIES_DETAILS_CSV_NAME = 'movies_details.csv'
MOVIES_CAST_CSV_NAME = 'movies_cast.csv'
MOVIES_REVIEWS_CSV_NAME = 'movies_reviews.csv'
CSV_PATH = './csv_files/'


def load_movies_details():
    data = pd.read_csv(CSV_PATH + MOVIES_DETAILS_CSV_NAME).T.to_dict()
    '''Load directors'''
    for i in range(len(data)):
        director_name = data[i]['Director']
        director_exist = Director.query.filter(Director.name == director_name).first()
        if not director_exist:
            db.session.add(Director(name=director_name))
            db.session.commit()
    for i in range(len(data)):
        ''' Load movies '''
        title = data[i]['Title']
        year = data[i]['Year']
        summary = data[i]['Movie summary']
        director = Director.query.filter(Director.name == director_name).first()
        new_movie = Movies(title=title, year=year, director=director.id, summary=summary)
        movie_exist = Movies.query.filter(Movies.title == new_movie.title and Movies.year == new_movie.year and Movies.director == new_movie.director).first()
        if not movie_exist:
            db.session.add(new_movie)
            db.session.commit()




def run_load(rootpath):
    global CSV_PATH
    CSV_PATH = rootpath+'/csv_files/'
    load_movies_details()