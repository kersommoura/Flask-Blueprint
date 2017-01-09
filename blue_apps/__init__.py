from flask import Flask

app = Flask(__name__)

from blue_apps.api.get_data import blue_api
from blue_apps.webapp.views import blue_webapp

app.register_blueprint(blue_api, url_prefix='/api')
app.register_blueprint(blue_webapp)