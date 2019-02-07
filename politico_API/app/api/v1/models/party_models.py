parties = []

class PartyModels():

    def __init__(self):

        self.db = parties

    #create party function.
    def create_party(self, name, hqAddress, logoUrl):
        party = {
            "party_id": len(self.db)+1,
            "name": name,
            "hqAddress": hqAddress,
            "logoUrl": logoUrl,
        }

        self.db.append(party)
        return party

    #retrieve all parties function.
    def get_all_parties(self):
        return self.db

    #get party function.
    def get_party_by_Id(self, party_id):
       if self.db:
           for party in self.db:
               if party.get('party_id') == party_id:
                   return party

    #delete party function.
    def remove_party(self, party_id):
        if self.db:
           for party in self.db:
               if party.get('party_id') == party_id:
                   self.db.remove(party)
                   return party

     #edit party function.            
    def edit_party(self, party_id):
         if self.db:
           for update_p in self.db:
               if update_p.get('party_id') == party_id:
                   return update_p


            
                    




    