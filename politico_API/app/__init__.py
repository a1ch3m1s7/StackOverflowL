from flask import Flask, Blueprint
from app.api.v1.views.parties.views import p_v1 as v1

def politico_app():

    app = Flask(__name__)

    app.register_blueprint(v1, url_prefix="/api/v1")

    return app
