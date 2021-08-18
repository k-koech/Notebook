from flask import Blueprint
# from . import views,

auth = Blueprint('auth',__name__)

from . import views,forms