from .models import db, Director, Movies, Ranking, Cast, MoviesCast, Reviews
import pandas as pd
from datetime import datetime
MOVIES_DETAILS_CSV_NAME = 'movies_details.csv'
MOVIES_CAST_CSV_NAME = 'movies_cast.csv'
MOVIES_REVIEWS_CSV_NAME = 'movies_reviews.csv'
CSV_PATH = './csv_files/'


def load_movies_details():
    '''Insert ranking date to database'''
    data = pd.read_csv(CSV_PATH + MOVIES_DETAILS_CSV_NAME).T.to_dict()
    # date_exist = RankingDate.query.filter(RankingDate.date == datetime.now().date()).first()
    # if not date_exist:
    #     db.session.add(RankingDate(date=datetime.now().date()))
    #     db.session.commit()
    '''Insert directors to database'''
    for i in range(len(data)):
        director_name = data[i]['Director']
        director_exist = Director.query.filter(Director.name == director_name).first()
        if not director_exist:
            db.session.add(Director(name=director_name))
            db.session.commit()
        ''' Insert movies to database '''
        title = data[i]['Title']
        year = data[i]['Year']
        summary = data[i]['Movie summary']
        director = Director.query.filter(Director.name == director_name).first()
        new_movie = Movies(title=title, year=year, director=director.id, summary=summary)
        movie_exist = Movies.query.filter(Movies.title == new_movie.title and Movies.year == new_movie.year and Movies.director == new_movie.director).first()
        if not movie_exist:
            db.session.add(new_movie)
            db.session.commit()
        db.session.close()
        '''Insert ranking to database'''
        date = datetime.now().date()
        movie_id = Movies.query.filter(Movies.title == title and Movies.year == year).first().id
        ranking_exist = Ranking.query.filter(Ranking.date == date or Ranking.movie_id == movie_id).first()
        if not ranking_exist:
            db.session.add(Ranking(movie_id=movie_id, ranking=data[i]['Ranking Position'], date=date))
            db.session.commit()
    db.session.close()
    

def load_movies_cast():
    '''Insert movies cast to database'''
    data = pd.read_csv(CSV_PATH + MOVIES_CAST_CSV_NAME).T.to_dict()
    for i in range(len(data)):
        name = data[i]['Cast']
        cast_exist = Cast.query.filter(Cast.name == name).first()
        if not cast_exist:
            db.session.add(Cast(name=name))
            db.session.commit()
        mov = Movies(title=data[i]['Title'])
        movie_id = Movies.query.filter(Movies.title == data[i]['Title'].strip()).first().id
        cast_id = Cast.query.filter(Cast.name == name).first().id
        moviecast_exist = MoviesCast.query.filter(MoviesCast.movie_id == movie_id and MoviesCast.cast_id == cast_id).first()
        if not moviecast_exist:
            db.session.add(MoviesCast(movie_id=movie_id, cast_id=cast_id))
            db.session.commit()
    db.session.close()


def load_movies_revews():
    ''' Insert movies revievs to database '''
    data = pd.read_csv(CSV_PATH + MOVIES_REVIEWS_CSV_NAME).T.to_dict()
    for i in range(len(data)):
        movie_id = Movies.query.filter(Movies.title == data[i]['Title'].strip()).first().id
        review = data[i]['Reviews'].strip()
        review_exist = Reviews.query.filter(Reviews.review == review).first()
        if not review_exist:
            db.session.add(Reviews(movie_id=movie_id, review=review))
            db.session.commit()
    db.session.close()


def run_load(rootpath):
    global CSV_PATH
    CSV_PATH = rootpath+'/csv_files/'
    load_movies_details()
    load_movies_cast()
    load_movies_revews()

