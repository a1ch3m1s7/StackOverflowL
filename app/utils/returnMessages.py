from flask import make_response, jsonify

def error(StatusCode, msg):
	return make_response(jsonify({
			"status": StatusCode,
			"error": msg
	}))

def success(StatusCode, data):
	return make_response(jsonify({
			"status": StatusCode,
			"success": data
	}))

def more_data_fields():
	return make_response(jsonify({

		"status": 400,
        "error": "Bad Query - More data fields than expected"
	}))

def few_data_fields():
	return make_response(jsonify({
		"status": 400,
        "error": "Bad Query - Fewer data fields than expected"
	}))

def data_already_exists(msg):
	return make_response(jsonify({
		"status": 409,
		"msg" : msg
	}))

def id_is_zero():
	return make_response(jsonify({
		"status": 400,
        "error": "ID cannot be zero or negative"

	}))
               
def id_out_of_range():
	return make_response(jsonify({
		"status": 416,
        "error": "ID out of range. Requested Range does not exist"
	}))
                    

def invalid_data():
	return make_response(jsonify({
		"status": 422,
        "error": "Unprocessable Entity - Invalid value in data field"

	}))
               
def empty_data_field():
	return make_response(jsonify({
		"status": 422,
        "error": "Empty data field"
	}))
                
def expected_party_fields():
	return make_response(jsonify({
		"name" : "name of party",
		"hqAddress" : "headquaters",
		"logoUrl": "logo url"
	}))


  	