"""Model for Genre"""
from book_app.database.db import db
from book_app.models.book import Book


class Genre(db.Model):
    __tablename__ = 'Genre'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    genre_book = db.relationship(Book, backref='Genre', lazy='dynamic')

    def __init__(self, name):
        self.name = name
