from flask import Blueprint

blue_api = Blueprint('blue_api', __name__)

@blue_api.route('/get_data')
def get_data_api():
    return '{"data": "data from api using blueprint"}'