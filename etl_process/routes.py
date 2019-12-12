from flask import current_app as app
from .models import db, Movies, reset_database


@app.route('/')
def hello():
    return "Hello World!"

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