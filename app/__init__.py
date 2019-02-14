from flask import Flask, make_response, jsonify
from app.api.v1.views.party_views import p_v1 as v1
from app.api.v1.views.office_views import office as v2


def page_not_found(e):
	"""Capture Not Found error."""
	
	return make_response(jsonify({
		"status" : "not found",
		"message" : "url does not exist"
		}), 404)

def method_not_allowed(e):
	"""Capture Not Found error."""
	
	return make_response(jsonify({
		"status" : "error",
		"message" : "method not allowed"
		}), 404)

def method_not_json(e):
	"""Capture Not Found error."""
	
	return make_response(jsonify({
		"status" : "bad request",
		"message" : "method not allowed, invalid json format"
		}), 400)


def create_app():
	app = Flask(__name__)
	app.register_blueprint(v1, url_prefix="/api/v1")
	app.register_blueprint(v2, url_prefix="/api/v1/")
	app.register_error_handler(400, method_not_json)
	app.register_error_handler(404, page_not_found)
	app.register_error_handler(405, method_not_allowed)

	return app
