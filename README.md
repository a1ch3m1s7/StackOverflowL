[![Build Status](https://travis-ci.com/a1ch3m1s7/Politico.svg?branch=develop)](https://travis-ci.com/a1ch3m1s7/Politico) [![Coverage Status](https://coveralls.io/repos/github/a1ch3m1s7/Politico/badge.svg?branch=develop)](https://coveralls.io/github/a1ch3m1s7/Politico?branch=develop) [![Maintainability](https://api.codeclimate.com/v1/badges/f2aa7312e96fc80a8a8f/maintainability)](https://codeclimate.com/github/a1ch3m1s7/Politico/maintainability)

# Politico
A platform that will enable citizens to give their mandate to politicians running for different government offices
while building trust in the process through transparency.


# API Endpoints.

This are the required endpoints...

| Requirements                        |
| ------------------------------------|
| ○ Create a political party.         |
| ○ Get all political parties.        |
| ○ Get a specific political party.   |
| ○ Edit a specific political party.  |
| ○ Delete a particular party.        |
| ○ Create a political office.        |
| ○ Get all political offices.        |
| ○ Get a specific political office.  |

## Required Features
1. An administrator should be able to crete a political party in Politico
2. An admin should be able to retrieve a particular office or party.
2. An admin should be able to delete a political party and office
3. Admin should be able to edit a party information

## Endpoints

Title | Endpoint | Method | Description
--- | --- | --- | ---
Create a party | /api/v1/parties | POST | An admin creates a party
Get all party | /api/v1/parties | GET | Get get all parties
Get specific party | /api/v1/parties/partyID | GET | Get a specific party
Edit specific party | /api/v1/edit/partyID | PATCH | Edit a specific party
Delete specific party | /api/v1/remove_party/partyID | DELETE | Delete a specific party
Create an office | /api/v1/offices | POST | An admin creates an office
Get all offices | /api/v1/offices/ | GET | Get all offices
Get specific office | /api/v1/office/office_id | GET | Get a specific office
Delete specific office | /api/v1/remove_office/<office_id> | DELETE | Get a specific office


# Installation and Setup
Clone the repository.
```
https://github.com/a1ch3m1s7/Politico.git
```

## Create a virtual environment

```
python3 -m venv venv;
source venv/bin/activate
```
If you need to install virtualenv:
```
virtualenv venv
```
## Creating an env file
create a ```.env``` file and insert the following code

```
source venv/bin/activate
export FLASK_APP="run.py"
export FLASK_ENV="development"
export APP_SETTIINGS="development"

```

## Activate the virtual environment
Before you begin you will need to activate the corresponding environment
```
source .env
```
## Install requirements
```
pip install -r requirements.txt
```

## Running the application
After the configuration, you will run the app 
```
export FLASK_APP=run.py
flask run
```
## Testing the app
To test the app, run the following

```
pytest
```

## Usage

I recommended using postman to send requests to the above detailed endpoints
### Party Endpoints
For this endpoint, minimum data required are as follows
```
{
  "id": 1,
  "name": "name of party",
  "hqAddress": "headquarters",
  "logoUrl": "imageUrl"
  
}
```
### Office Endpoints
For this endpoint, minimum data required are as follows
```
{
  "id": 1,
  "type": "type of office",
  "name": "name of the office"
}
```

## Heroku deployment site.
For parties .https://a1ch3m1s7-politico.herokuapp.com/api/v1/parties.
For offices .https://a1ch3m1s7-politico.herokuapp.com/api/v1/offices.

## Contributing
Contributions are highly encouraged, please open an issue to discuss what you would like to change and with what.
For the test please update them to your specific needs.




