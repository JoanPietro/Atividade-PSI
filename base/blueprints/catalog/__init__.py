from flask import Blueprint
from . import routes

catalog_bp = Blueprint("catalog", __name__, template_folder="templates")

