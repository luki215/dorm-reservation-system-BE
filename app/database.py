from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import create_database, database_exists
from os import environ
from app import db, db_url



def init_db():
    if not database_exists(db_url):
        create_database(db_url)

    import models.user
    db.create_all()

def seed_data():
    from models.user import User
    user = User(name="Example", email="mail@example.com", password="123456" )

    db.session.add(user)
    db.session.commit()
