from flask import Blueprint

blue_webapp = Blueprint('blue_webapp', __name__)

@blue_webapp.route('/')
def homepage():
    return "Homepage"