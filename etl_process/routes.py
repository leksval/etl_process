from flask import current_app as app
from .models import db, Movies, reset_database, MoviesCast, Director, Cast, Reviews, Ranking
from flask import render_template, request
from .extract_part.extract import run_extract
from .transform_part.transform import run_transform
from .load import run_load


@app.route('/')
def home():
    print(app.root_path)
    print(app.instance_path)
    return render_template("home.html")

@app.route('/etl')
def etl_page():
    return render_template("etlpage.html")


@app.route('/ranking')
def ranking_page():
    ranking = Ranking.query.all()
    movies = Movies.query.all()
    director = Director.query.all()
    print(len(ranking))
    return render_template("ranking.html",
        ranking=ranking,
        movies=movies,
        director=director,
        datalength=len(ranking))


@app.route('/reset')
def reset_db():
    reset_database()
    return 'aaa'


@app.route('/extract', methods=['POST'])
def extract_imdb():
    movie_quantity = request.form['movieQuantity']
    reviews_quantity = request.form['reviewsQuantity']
    cast_quantity = request.form['castQuantity']
    run_extract(movie_quantity, reviews_quantity, cast_quantity, app.root_path)
    return 'Success'


@app.route('/fulletl', methods=['POST'])
def etl_imdb():
    movie_quantity = request.form['movieQuantity']
    reviews_quantity = request.form['reviewsQuantity']
    cast_quantity = request.form['castQuantity']
    run_extract(movie_quantity, reviews_quantity, cast_quantity, app.root_path)
    run_transform(app.root_path)
    run_load(app.root_path)
    return 'Success'


@app.route('/transform')
def transform_imdb():
    run_transform(app.root_path)


@app.route('/load')
def load_imdb():
    run_load(app.root_path)
    return 'load'
