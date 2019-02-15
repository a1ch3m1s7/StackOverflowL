
""" imports """
from app.api.v1.models.party_models import PartyModels
import json
import re
from app.utils.returnMessages import success, error


class validate:
    
    """ def check_keys(self, request):
        Check if the key values are correct.
        input_keys = ['name', 'hqAddress', 'logoUrl']
        invalid = []
        for key in input_keys:
            if not key in request.json:
                invalid.append(key)
                return invalid"""

    def valid_email(self, var):
        """ Check if email is a valid mail. """

        if re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+[a-zA-Z0-9-.]+$)",var):
            return True
        return False 


    def valid_url(self, var):
        """Check if email is valid."""

        if re.match(r"https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)", var):
            return True
        return False


    