"""
Module contains all application routes
"""
from flask import current_app as app
from .models import db, Movies, reset_database, MoviesCast, Director, Cast, Reviews, Ranking
from flask import render_template, request, redirect
from .extract_part.extract import run_extract
from .transform_part.transform import run_transform
from .load import run_load
from datetime import datetime, date


@app.route('/')
def home():
    """ Render home page"""
    return render_template("home.html")


@app.route('/etl')
def etl_page():
    """ Render etl process page""" 
    return render_template("etlpage.html")


@app.route('/ranking')
def ranking_page():
    """ Render ranking page"""
    ranking = Ranking.query.all()
    movies = Movies.query.all()
    director = Director.query.all()
    return render_template("ranking.html",
        ranking=ranking,
        movies=movies,
        director=director,
        title = 'Ranking')


@app.route('/reset')
def reset_db():
    """ Helper route to reset database"""
    reset_database()
    return redirect('/etl')


@app.route('/extract', methods=['POST'])
def extract_imdb():
    """Route to extract data from imdb and render transform page"""
    movie_quantity = int(request.form['movieQuantity'])
    reviews_quantity = int(request.form['reviewsQuantity'])
    cast_quantity = int(request.form['castQuantity'])
    count = run_extract(movie_quantity, reviews_quantity, cast_quantity, app.root_path)
    return render_template("transform.html", count=count)


@app.route('/fulletl', methods=['POST'])
def etl_imdb():
    movie_quantity = int(request.form['movieQuantity'])
    reviews_quantity = int(request.form['reviewsQuantity'])
    cast_quantity = int(request.form['castQuantity'])
    run_extract(movie_quantity, reviews_quantity, cast_quantity, app.root_path)
    run_transform(app.root_path)
    run_load(app.root_path)
    return redirect('/ranking')


@app.route('/transform')
def transform_imdb():
    """Route to transform data from imdb and redirect to load data page"""
    run_transform(app.root_path)
    return render_template("load.html")


@app.route('/load')
def transform_and_load_imdb():
    """Route to transform data from imdb and insert data into database"""

    run_load(app.root_path)
    ranking = Ranking.query.filter(Ranking.date == datetime.now().date()).all()
    movies = Movies.query.all()
    director = Director.query.all()
    return render_template("ranking.html",
        ranking=ranking,
        movies=movies,
        director=director,
        title ='Loaded data')


@app.route('/movies')
def show_movies():
    """Show movies from database"""
    movies = Movies.query.all()
    director = Director.query.all()
    return render_template("movies.html",
        movies=movies,
        director=director)

@app.route('/movie/<id>')
def show_movie_details(id=None):
    """Show movie details by movie id"""
    movie = Movies.query.filter(Movies.id == id).first()
    director = Director.query.filter(Director.id == movie.director).first()
    reviews = Reviews.query.filter(Reviews.movie_id == movie.id).all()
    movies_cast = MoviesCast.query.filter(MoviesCast.movie_id == movie.id).all()
    cast = Cast.query.all()
    ranking = Ranking.query.filter(Ranking.movie_id == movie.id).all()
    return render_template('movie.html',
        id=id,
        movie=movie,
        director=director,
        reviews=reviews,
        moviesCast=movies_cast,
        ranking=ranking)