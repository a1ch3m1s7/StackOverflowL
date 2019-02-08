parties = []

class PartyModels():

    def __init__(self):

        self.db = parties

    def create_party(self, name, hqAddress, logoUrl):
        party = {
            "party_id": len(self.db)+1,
            "name": name,
            "hqAddress": hqAddress,
            "logoUrl": logoUrl,
        }

        self.db.append(party)
        return party

    def get_all_parties(self):
        return self.db

    def get_party_by_Id(self, party_id):
       if self.db:
           for party in self.db:
               if party.get('party_id') == party_id:
                   return party

    def remove_party(self, party_id):
        if self.db:
           for party in self.db:
               if party.get('party_id') == party_id:
                   self.db.remove(party)
                   return party


    

    def edit_party(self, parties):
        if self.db:
            for party in self.db:
                if party['party_id'] == parties:
                    # return party
                    party["party_id"] = parties["party_id"]
                    party["name"] = parties["name"]
                    party["hqAddress"] = parties["hqAddress"]
                    party["logoUrl"] = parties["logoUrl"]
                return parties