# app.py - a minimal flask api using flask_restful
from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS

from os import environ
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
CORS(app)
api = Api(app)


# db 
db_url = f"postgresql://{environ['POSTGRES_USER']}:{environ['POSTGRES_PASSWORD']}@{environ['PG_HOST']}/dormsDB"
app.config['SQLALCHEMY_DATABASE_URI'] = db_url
db = SQLAlchemy(app)



# init resources 
from resources.login import Login
api.add_resource(Login, '/login')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')