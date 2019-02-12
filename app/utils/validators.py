from app.api.v1.models.party_models import PartyModels
import json
from flask import make_response, jsonify, request


class validate:

    @classmethod
    def check_party_if_exist(cls):
        data = request.get_json()
        name = data['name']
        hqAddress = data['hqAddress']
        logoUrl = data['logoUrl']

        if not PartyModels().exists(name):

            new_party = PartyModels().create_party(name, hqAddress, logoUrl)
            return make_response(jsonify({
                "msg": "party created succefully",
                "party" : new_party
                }), 201)
        else:
            return make_response(jsonify({
                "valid": True,
                "data": {
                    "status": 409,
                    "error": "Conflict. Party already exists"
                }
            }))

  
