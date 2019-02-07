from flask import request, Blueprint, make_response, jsonify
from app.api.v1.models.office_models import officeModels
import json
office = Blueprint('v2', __name__, url_prefix='/api/v1/')

@office.route('/offices', methods=['POST'])
def create_office():
    data = request.get_json()
    data_id = data['id']
    N_type  = data['type']
    name = data['name']

    officeModels().create_office(data_id, N_type, name)

    return make_response(jsonify({
        "msg": "office created succefully"
}))         

#get all offices
@office.route('/offices', methods=['GET'])
def get_offices():
    offices = []
    offices = officeModels().get_all_offices()

    if offices:
        return jsonify({
            "msg" : "success",
            "parties" : offices
        })
    return jsonify({
        "msg" : "success",
        "parties": offices
    })

@office.route('/offices/<int:office_id>', methods=['GET'])
def get_office_by_id(office_id):
        office = officeModels().get_office_by_Id(office_id)

        if office:
            return jsonify({
                "msg" : "success",
                "party" : office
            })
        return jsonify({
            "msg" : "404 error",
        })