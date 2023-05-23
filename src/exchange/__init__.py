from flask import Blueprint

exchange = Blueprint("exchange", __name__, url_prefix="/exchange")

from src.exchange import routes