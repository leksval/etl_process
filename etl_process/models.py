from . import db


def reset_database():
    db.reflect()
    db.drop_all()
    db.create_all()


# movies_cast = db.Table('movies_cast', db.Column('movies_id', db.Integer, db.ForeignKey('movies.id'), primary_key=True),
#     db.Column('cast_id', db.Integer, db.ForeignKey('cast.id'), primary_key=True))

# movies_ranking = db.Table('movies_ranking', db.Column('movies_id', db.Integer, db.ForeignKey('movies.id'), primary_key=True),
#     db.Column('ranking_id', db.Integer, db.ForeignKey('ranking.id'), primary_key=True))

class MoviesCast(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, index=False, nullable=False)
    cast_id = db.Column(db.Integer, index=False, nullable=False)

class MoviesRanking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, index=False, nullable=False)
    ranking = db.Column(db.Integer, index=False, nullable=False)
    date_id = db.Column(db.Integer, index=False, nullable=False)

class Movies(db.Model):
    __tablename__ = 'movies'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), index=True, nullable=False)
    year = db.Column(db.Integer, index=True, nullable=False)
    director = db.Column(db.Integer, index=False, nullable=False)
    summary = db.Column(db.Text, unique=True, index=False, nullable=False)

class Director(db.Model):
    __tablename__ = 'director'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255),unique=True, index=True, nullable=False)

class Cast(db.Model):
    __tablename__ = 'cast'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255),unique=True, index=True, nullable=False)


class Reviews(db.Model):
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True)
    review = db.Column(db.Text,unique=True, index=False, nullable=False)
    movie_id = db.Column(db.Integer,unique=False, index=False, nullable=False)


class RankingDate(db.Model):
    __tablename__ = 'rankingdate'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, unique=True, nullable=False)