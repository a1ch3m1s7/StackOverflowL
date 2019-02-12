parties = []

class PartyModels():

    @staticmethod
    def exists(name):
        """  """
        for party in parties:
            if party["name"] == name:
                return True
        return False


    def create_party(self, name, hqAddress, logoUrl):
        party = {
            "party_id": len(parties)+1,
            "name": name,
            "hqAddress": hqAddress,
            "logoUrl": logoUrl,
        }

        parties.append(party)
        return party

    def get_all_parties(self):
        return parties

    def get_party_by_Id(self ,party_id):
       if parties:
           for party in parties:
               if party.get('party_id') == party_id:
                   return party

    def remove_party(self, party_id):
        if parties:
           for party in parties:
               if party.get('party_id') == party_id:
                   parties.remove(party)
                   return party

    def edit_party(self, parties, party_id):
        """ edits parties """
        for party in parties:
                if party['party_id'] == party_id:
                    name = parties.get('name')
                    hqAddress = parties.get('hqAddress')
                    logoUrl = parties.get('logoUrl')
                    if name:
                        party['name']  = name
                    if hqAddress:
                        party['hqAddress'] = hqAddress
                    if logoUrl:
                        party['logoUrl'] = logoUrl
                    return party