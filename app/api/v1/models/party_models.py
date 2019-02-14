import json
parties = []

class PartyModels():

    def __init__(self):
        self.parties = parties

    def create_party(self, name, hqAddress, logoUrl):
        party = {
            "party_id": len(self.parties)+1,
            "name": name,
            "hqAddress": hqAddress,
            "logoUrl": logoUrl,
        }

        self.parties.append(party)
        return party

    def get_name(self, name):
        """Get a party with a specific name."""
        for party in self.parties:
            if party['name'] == name:
                return json.dumps(party, default=str)

    def get_hqAddress(self, hqAddress):
        """Get party by hqAddress."""
        for party in self.parties:
            if party['hqAddress'] == hqAddress:
                return json.dumps(party, default=str)

    def get_logoUrl(self, logoUrl):
        """Get party by logoUrl."""

        for party in self.parties:
            if party['logoUrl'] == logoUrl:
                return json.dumps(party, default=str)

    def get_all_parties(self):
        return self.parties

    def get_party_by_Id(self ,party_id):
       if parties:
           for party in self.parties:
               if party.get('party_id') == party_id:
                   return party

    def remove_party(self, party_id):
        if parties:
           for party in self.parties:
               if party.get('party_id') == party_id:
                   parties.remove(party)
                   return party

    def update_party(self, party_id, details):
        """Updates an existing party."""
        for party in self.parties:
            if party['party_id'] == party_id:
                name = details.get('name')
                hqAddress = details.get('hqAddress')
                logoUrl = details.get('logoUrl')
                if name:
                    party['name']  = name
                if hqAddress:
                    party['hqAddress'] = hqAddress
                if logoUrl:
                    party['logoUrl'] = logoUrl
                return party
