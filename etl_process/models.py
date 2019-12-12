# from sqlalchemy.dialects import postgresql
from . import db
from flask import current_app as app
from sqlalchemy_utils import database_exists, create_database, drop_database

def reset_database():
    db.reflect()
    db.drop_all()
    db.create_all()


movies_cast = db.Table('movies_cast', db.Column('movies_id', db.Integer, db.ForeignKey('movies.id'), primary_key=True), db.Column('cast_id', db.Integer, db.ForeignKey('cast.id'), primary_key=True))


class Movies(db.Model):
    __tablename__ = 'movies'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), index=True, unique=False, nullable=False)
    year = db.Column(db.String(4), index=True, unique=False, nullable=False)
    director = db.Column(db.String(100), index=True, unique=False, nullable=False)
    summary = db.Column(db.Text, index=True, unique=False, nullable=False)
    cast = db.relationship('Cast', secondary=movies_cast)


class Cast(db.Model):
    __tablename__ = 'cast'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), index=True, unique=True, nullable=False)


