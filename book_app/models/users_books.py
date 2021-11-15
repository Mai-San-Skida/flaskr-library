from book_app.database.db import db


users_books = db.Table(
    'users_books',
    db.Column('user_id', db.Integer(), db.ForeignKey('User.id')),
    db.Column('book_id', db.Integer(), db.ForeignKey('Book.id'))
)
