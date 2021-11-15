import os

from flask import Flask
from flask_migrate import Migrate

from book_app.database.db import db


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI=f'sqlite:///{app.instance_path}/app.db',
    )

    migrate = Migrate(app, db)

    try:
        os.makedirs(app.instance_path)
    except IOError:
        pass

    db.init_app(app)
    with app.app_context():
        db.create_all()
        db.session.commit()

    @app.route('/')
    def index():
        return 'Index page.'

    return app
