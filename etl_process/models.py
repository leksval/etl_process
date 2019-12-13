from . import db


def reset_database():
    db.reflect()
    db.drop_all()
    db.create_all()


movies_cast = db.Table('movies_cast', db.Column('movies_id', db.Integer, db.ForeignKey('movies.id'), primary_key=True), db.Column('cast_id', db.Integer, db.ForeignKey('cast.id'), primary_key=True))


class Movies(db.Model):
    __tablename__ = 'movies'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), index=True, nullable=False)
    year = db.Column(db.Integer, index=True, nullable=False)
    director = db.Column(db.String(100), index=True, nullable=False)
    summary = db.Column(db.Text, index=False, nullable=False)
    cast = db.relationship('Cast', secondary=movies_cast)
    reviews = db.relationship("Reviews")


class Cast(db.Model):
    __tablename__ = 'cast'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), index=True, nullable=False)


class Reviews(db.Model):
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True)
    review = db.Column(db.Text, index=False, nullable=False)
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.id'))


class Ranking(db.Model):
    __tablename__ = 'ranking'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)