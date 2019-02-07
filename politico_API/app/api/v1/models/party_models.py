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