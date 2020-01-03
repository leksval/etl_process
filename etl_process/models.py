from . import db


def reset_database():
    """
    Remove all data from database and recreate tables for fresh use
    """
    db.reflect()
    db.drop_all()
    db.create_all()


class MoviesCast(db.Model):
    """
    Movie cast table model
    """
    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, index=False, nullable=False)
    cast_id = db.Column(db.Integer, index=False, nullable=False)


class Ranking(db.Model):
    """
    Ranking table model
    """
    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, index=False, nullable=False)
    ranking = db.Column(db.Integer, index=False, nullable=False)
    date = db.Column(db.Date, index=False, unique=False, nullable=False)


class Movies(db.Model):
    """
    Movies table model
    """
    __tablename__ = 'movies'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), index=True, nullable=False)
    year = db.Column(db.Integer, index=True, nullable=False)
    director = db.Column(db.Integer, index=False, nullable=False)
    summary = db.Column(db.Text, unique=True, index=False, nullable=False)


class Director(db.Model):
    """
    Director table model
    """
    __tablename__ = 'director'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, index=True, nullable=False)


class Cast(db.Model):
    """
    Cast table model
    """
    __tablename__ = 'cast'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, index=True, nullable=False)


class Reviews(db.Model):
    """
    CaReviews table model
    """
    __tablename__ = 'reviews'
    id = db.Column(db.BigInteger, primary_key=True, index=False)
    review = db.Column(db.Text, unique=False, index=False, nullable=False)
    movie_id = db.Column(db.Integer, unique=False, index=False, nullable=False)
