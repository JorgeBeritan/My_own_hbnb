from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
import os

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'katanga-master'

if os.getenv('FLASK_ENV') == 'development':
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
elif os.getenv('FLASK_ENV') == 'production':
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:your_password@localhost/hbnb'
    app.config['DEBUG'] = True

bcrypt = Bcrypt(app)
jwt = JWTManager(app)
db = SQLAlchemy(app)
