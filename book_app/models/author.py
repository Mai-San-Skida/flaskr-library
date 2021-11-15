"""Model for Author"""
from book_app.database.db import db
from book_app.models.book import Book


class Author(db.Model):
    __tablename__ = 'Author'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    surname = db.Column(db.String, nullable=False)

    author_book = db.relationship(Book, backref='Author', lazy='dynamic')

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
