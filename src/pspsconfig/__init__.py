from flask import Blueprint

configuration = Blueprint("configuration", __name__, url_prefix="/configuration")

from src.pspsconfig import routes