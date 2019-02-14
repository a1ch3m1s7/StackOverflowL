import json
offices = []

class officeModels():

    def __init__(self):

        self.office_data = offices

    def create_office(self, N_type, name):
        office = {
            "office_id": len(self.office_data)+1,
            "type" : N_type,
            "name": name
        }

        self.office_data.append(office)
        return office

    def get_type(self, N_type):
        """Get a party with a specific name."""
        for office in self.office_data:
            if office['type'] == N_type:
                return json.dumps(office, default=str)

    def get_name(self, name):
        """Get party by hqAddress."""
        for office in self.office_data:
            if office['name'] == name:
                return json.dumps(office, default=str)

    def get_all_offices(self):
        return self.office_data

    def get_office_by_Id(self, office_id):
       if self.office_data:
           for office in self.office_data:
               if office.get('office_id') == office_id:
                   return office

    def remove_office(self, office_id):
        if self.office_data:
           for offices in self.office_data:
               if offices.get('office_id') == office_id:
                   self.office_data.remove(offices)
                   return offices