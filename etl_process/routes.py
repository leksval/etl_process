from flask import current_app as app
from .models import db, Movies, reset_database
from flask import render_template
from .extract_part.extract import run_extract
from .transform_part.transform import run_transform
from .load import run_load
@app.route('/')
def home():
    print(app.root_path)
    print(app.instance_path)
    return render_template("home.html")

@app.route('/test')
def create_movie():
    title = 'John'
    year = '2011'
    director = 'Elton'
    summary = 'pop'
    new_movie = Movies(title=title, year=year, director=director, summary=summary)
    db.session.add(new_movie)
    db.session.commit()

@app.route('/reset')
def reset_db():
    reset_database()
    return 'aaa'

@app.route('/extract')
def extract_imdb():
    run_extract(3,2,2, app.root_path)
    return 'Success'

@app.route('/transform')
def transform_imdb():
    run_transform(app.root_path)

@app.route('/load')
def load_imdb():
    run_load(app.root_path)
    return 'load'
