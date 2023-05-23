from flask import Flask
from utils.db import db
from config import DATABASE_CONECTION_URI
from src.pspsconfig import configuration
from src.exchange import exchange

app = Flask(__name__)

app.secret_key = "development"
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_CONECTION_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

app.register_blueprint(configuration)
app.register_blueprint(exchange)