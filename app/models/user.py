from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.sql import expression
from app import db
import secrets

class User(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(120), unique=True)
    password = Column(String(120))
    auth_token = Column(String(120), unique=True, index=True)
    admin = Column(Boolean, server_default=expression.false(), nullable=False)

    def __init__(self, name=None, email=None, password=None, auth_token=secrets.token_urlsafe(), admin=False):
        self.name = name
        self.email = email
        self.password = password
        self.auth_token = auth_token
        self.admin = False

    @staticmethod
    def get(email=None): 
        return User.query.filter_by(email=email).first()