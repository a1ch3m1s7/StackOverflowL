<<<<<<< HEAD:app/__init__.py
from flask import Flask
from app.api.v1.views.party_views import p_v1 as v1
from app.api.v1.views.office_views import office as v2
=======
from flask import Flask, Blueprint
from politico_API.app.api.v1.views.party_views import p_v1 as v1
from politico_API.app.api.v1.views.office_views import office as v2
>>>>>>> 587fa98fc895523bb13b3ca8c9def9a00346bcb7:politico_API/app/__init__.py

def politico_app():
    app = Flask(__name__)
    app.register_blueprint(v1, url_prefix="/api/v1")
    app.register_blueprint(v2, url_prefix="/api/v1/")
    return app
