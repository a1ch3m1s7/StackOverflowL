from flask import Flask, Blueprint
from politico_API.app.api.v1.views.party_views import p_v1 as v1
from politico_API.app.api.v1.views.office_views import office as v2

def politico_app():
    app = Flask(__name__)
    app.register_blueprint(v1, url_prefix="/api/v1")
    app.register_blueprint(v2, url_prefix="/api/v1/")
    return app
