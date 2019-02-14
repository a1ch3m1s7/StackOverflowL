from flask import request, Blueprint, make_response, jsonify
from app.api.v1.models.party_models import PartyModels
from app.utils.validators import validate
from app.utils.returnMessages import success, error, more_data_fields, expected_party_fields, data_already_exists, few_data_fields, id_is_zero, id_out_of_range,invalid_data, empty_data_field
import json

p_v1 = Blueprint('v1', __name__, url_prefix='/api/v1')

parties = []

@p_v1.route('/parties', methods=['POST'])
def check_party_if_exist():
    data = request.get_json()
    name = data['name']
    hqAddress = data['hqAddress']
    logoUrl = data['logoUrl']

    if len(data) > 3:
        return more_data_fields()
    if len(data) < 3:
        return few_data_fields()
    elif PartyModels().get_name(name) or PartyModels().get_hqAddress(hqAddress) or PartyModels().get_logoUrl(logoUrl):
        return data_already_exists("Error : Party already exists")

    elif not validate().valid_url(logoUrl):
        return invalid_data()

    elif data['name'].isalpha() is False or data['hqAddress'].isalpha() is False:
        return invalid_data()
    else:
        res = PartyModels().create_party(name, hqAddress, logoUrl)
        return success(200, res)      


    #get all parties
@p_v1.route('/parties', methods=['GET'])
def get_parties():
    parties = PartyModels().get_all_parties()
    if parties:
            return success(201, parties)

    return error(502, "Bad gateway no data avaible")

@p_v1.route('/parties/<int:party_id>', methods=['GET'])
def get_parties_id(party_id):
        party = PartyModels().get_party_by_Id(party_id)

        if party:
            return success(201, party)
        return error(404, "party doesn't exist")

@p_v1.route('parties/remove_party/<int:party_id>', methods=['DELETE'])
def delete_party(party_id):
        party = PartyModels().remove_party(party_id)
        if party:
                return success(201, party)
        return error(404, "could not delete party")

@p_v1.route('parties/edit/<int:party_id>',methods=['PATCH'])
def edit_party(party_id):
    """Edit a specific party."""

    details = request.get_json()
    party = PartyModels().update_party(party_id, details)
    if party:
        n_success = make_response(jsonify({
            "status" : 200,
            "mg": "party updated successfully",
            "data": party
        }))
        return n_success
    return make_response(jsonify({
        "status": "not found"
    }), 404)
