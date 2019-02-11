""" third party imports """

from flask import request, Blueprint, make_response, jsonify
from app.api.v1.models.office_models import officeModels
import json
office = Blueprint('v2', __name__, url_prefix='/api/v1/')

offices = []

@office.route('/offices', methods=['POST'])
def create_office():
    """ This route enables the admin to create an office """
    data = request.get_json()
    data_id = data['id']
    N_type  = data['type']
    name = data['name']

    officeModels().create_office(data_id, N_type, name)

    return make_response(jsonify({
        "msg": "office created succefully"
}), 200)         


#get all offices
@office.route('/offices', methods=['GET'])
def get_offices():

    """ This route enables the admin to get all office """

    offices = officeModels().get_all_offices()
    if offices:
        return jsonify({
            "msg" : "success",
            "offices" : offices
        })
    return jsonify({
        "msg" : "success",
        "offices": offices
    })

@office.route('/offices/<int:office_id>', methods=['GET'])
def get_office_by_id(office_id):
    """ This route enables the admin to get a specific office """

    offices = officeModels().get_office_by_Id(office_id)

    if offices:
        return jsonify({
            "msg" : "success",
            "offices" : offices
        })
    return jsonify({
        "msg" : "404 error",
    })


@office.route('/remove_office/<int:office_id>', methods=['DELETE'])
def delete_office(office_id):
    """ This route enables the admin to delete party  """

    get_office = officeModels().remove_office(office_id)
    if get_office:
        return jsonify({
            "msg" : "successfully deleted",
            "offices" : get_office
        })
    return jsonify({
        "msg" : "Could not delete the party "
    })
