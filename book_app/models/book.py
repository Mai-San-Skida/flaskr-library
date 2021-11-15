"""Model for Book"""
from book_app.database.db import db


class Book(db.Model):
    __tablename__ = 'Book'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, default='No description.')

    author_id = db.Column(db.Integer, db.ForeignKey('Author.id'), nullable=False)
    genre_id = db.Column(db.Integer, db.ForeignKey('Genre.id'), nullable=False)

    def __init__(self, name, author_id, genre_id):
        self.name = name

        self.author_id = author_id
        self.genre_id = genre_id
