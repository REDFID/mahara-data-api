from flask import Blueprint

from .settings import *
from .database import *

views = Blueprint('views', __name__)


@views.route("/test", methods=["GET"])
def test_view():
    return {"msg": "hola!"}