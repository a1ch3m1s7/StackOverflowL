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
