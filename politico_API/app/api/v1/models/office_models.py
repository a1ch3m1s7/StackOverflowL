offices = []

class officeModels():

    def __init__(self):

        self.office_data = offices

    def create_office(self, data_id, N_type, name):
        office = {
            "office_id": len(self.office_data)+1,
            "id" : data_id,
            "type" : N_type,
            "name": name,
        }

        self.office_data.append(office)
        return self.office_data

    