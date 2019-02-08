import unittest
import json
from app import politico_app


class TestParty(unittest.TestCase):
    def setUp(self):
        self.app = politico_app() 
        self.client = self.app.test_client()
        self.data = {
            "party_id" : 1,
            "name": "jubilee",
            "hqAddress": "thika",
            "logoUrl": "jubilee.png"
        }


    def tearDown(self):
            self.app = None
            self.client = None
            self.data = {}

    def test_post_to_party(self):
        """ Tests create a party """

        response = self.client.post(
            'api/v1/parties',
            data=json.dumps(self.data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 201)

    def test_get_all_parties(self):
        """Test retrival of all parties"""
        response = self.client.get('api/v1/parties')
        self.assertEqual(response.status_code, 200)

    def test_get_specific_party(self):
        """ Tests retrieve a specific party """
        response = self.client.get('api/v1/parties/1')
        self.assertEqual(response.status_code, 200)

    def test_edit_no_party(self):
        """ Tests the response on a non-existant resource  """

        response = self.client.put('api/v1/edit')
        self.assertEqual(response.status_code, 404)

    def tests_delete_party(self):
        """ Tests the delete party route  """

        response = self.client.delete('api/v1/remove_party/1')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()