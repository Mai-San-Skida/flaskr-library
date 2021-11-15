"""Model for User"""
from book_app.database.db import db
from book_app.models.users_books import users_books
from book_app.models.book import Book


class User(db.Model):
    __tablename__ = 'User'

    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    surname = db.Column(db.String, nullable=False)

    favorite_books = db.relationship(Book, secondary=users_books, backref=db.backref('book', lazy='dynamic'))

    def __init__(self, login, email, password, name, surname):
        self.login = login
        self.email = email
        self.password = password
        self.name = name
        self.surname = surname
