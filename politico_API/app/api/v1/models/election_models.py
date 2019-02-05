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

