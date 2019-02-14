import json
import unittest

# Local imports
from app import create_app


class TestOffice(unittest.TestCase):

    def setUp(self):
        self.app = create_app() 
        self.client = self.app.test_client()
        self.data = {
          "type": "presidential",
          "name": "jubilee"
        }


    """ This class handles methods to test version 1 of the api """

    def test_post_to_office(self):
        """ Tests create an office """

        response = self.client.post(
            'api/v1/offices',
            data=json.dumps(self.data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)

    #
    def test_retrieve_all_offices(self):
        """ Tests retrieve all offices"""

        response = self.client.get('api/v1/offices')
        self.assertEqual(response.status_code, 200)

    def test_retrieve_specific_office(self):
        """ Tests retrieve specific office """

        response = self.client.get('api/v1/offices/1')
        self.assertEqual(response.status_code, 200)

    def tests_delete_office(self):
        """ Tests the delete party route  """

        response = self.client.delete('api/v1/offices/remove_office/1')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
    
