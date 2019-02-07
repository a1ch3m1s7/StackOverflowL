from flask import request, Blueprint, make_response, jsonify
from politico_API.app.api.v1.models.party_models import PartyModels
import json
p_v1 = Blueprint('v1', __name__, url_prefix='/api/v1')


@p_v1.route('/parties', methods=['POST'])
def create_party():
    data = request.get_json()
    name = data['name']
    hqAddress = data['hqAddress']
    logoUrl = data['logoUrl']

    PartyModels().create_party(name, hqAddress, logoUrl)

    return make_response(jsonify({
        "msg": "party created succefully"
}))         


    #get all parties
@p_v1.route('/parties', methods=['GET'])
def get_parties():
    parties = []
    parties = PartyModels().get_all_parties()

    if parties:
        return jsonify({
            "msg" : "success",
            "parties" : parties
        })
    return jsonify({
        "msg" : "success",
        "parties": parties
    })

@p_v1.route('/parties/<int:party_id>', methods=['GET'])
def get_parties_id(party_id):
        party = PartyModels().get_party_by_Id(party_id)

        if party:
            return jsonify({
                "msg" : "success",
                "party" : party
            })
        return jsonify({
            "msg" : "404 error",
        })

@p_v1.route('/remove_party/<int:party_id>', methods=['DELETE'])
def delete_party(party_id):
        party = PartyModels().remove_party(party_id)
        if party:
                return jsonify({
                    "msg" : "successfully deleted",
                    "parties" : party
                })
        return jsonify({
            "msg" : "Could not delete the party "
        })

@p_v1.route('/edit/<int:party_id>',methods=['PATCH'])
def edit_party(party_id):
    parties = request.get_json()
    party = PartyModels().edit_party(parties)
    return make_response(jsonify({
        "message": "Success!! Party patched",
        "data": party
}))

