""" third party imports """
from flask import request, Blueprint, make_response, jsonify
import json

""" local imports """
from app.api.v1.models.office_models import officeModels
from app.utils.returnMessages import success, error, more_data_fields, few_data_fields,data_already_exists, id_is_zero, id_out_of_range,invalid_data, empty_data_field

office = Blueprint('v2', __name__, url_prefix='/api/v1/')

offices = []

@office.route('/offices', methods=['POST'])
def check_party_if_exist():
    try:
        data = request.get_json()
        N_type  = data['type']
        name = data['name']

        if len(data) > 2:
            return more_data_fields()
        elif len(data) < 2:
            return few_data_fields()
        elif officeModels().get_type(N_type) or officeModels().get_name(name):
            return data_already_exists("Error : office already exists")
        elif data['name'].isalpha() is False or data['type'].isalpha() is False:
            return invalid_data()
        else:
            res = officeModels().create_office(name, N_type)
            return success(200, res) 
    except(TypeError, KeyError, ValueError):
        res =jsonify({"message": "missing parameters"})
        return res
#get all offices
@office.route('/offices', methods=['GET'])
def get_offices():

    """ This route enables the admin to get all office """

    offices = officeModels().get_all_offices()
    if offices:
        return success(200, offices)
    return error(404, "Office doesn't exists")
    

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


@office.route('/offices/remove_office/<int:office_id>', methods=['DELETE'])
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


