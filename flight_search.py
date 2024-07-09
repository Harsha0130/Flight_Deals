import requests
import os
from datetime import datetime

AMADEUS_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"
AMADEUS_API_KEY = os.environ["AMADEUS_API_KEY"]
AMADEUS_API_SECRET = os.environ["AMADEUS_API_SECRET"]
TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"
IATA_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.api_key = AMADEUS_API_KEY
        self.api_secret_key = AMADEUS_API_SECRET
        self.token = self.get_new_token()

    def get_new_token(self):
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        body = {
            'grant_type': 'client_credentials',
            'client_id': self.api_key,
            'client_secret': self.api_secret_key,
        }
        response = requests.post(url=TOKEN_ENDPOINT, headers=header, data=body)

        # New bearer token. Typically expires in 1799 seconds (30min)
        print(f"Your token is {response.json()['access_token']}")
        print(f"Your token expires in {response.json()['expires_in']} seconds")
        return response.json()['access_token']

    def get_destination_code(self, city_name):
        headers = {"Authorization": f"Bearer {self.token}"}
        query = {
            "keyword": city_name,
            "max": "2",
            "include": "AIRPORTS",
        }

        print(f"Requesting IATA code for city: {city_name}")
        response = requests.get(url=IATA_ENDPOINT, headers=headers, params=query)
        response.raise_for_status()
        print(f"Status_code: {response.status_code}")
        print(f"Response: {response.json()}")

        try:
            code = response.json()["data"][0]['iataCode']
        except (IndexError, KeyError) as e:
            print(f"Error: No IATA code found for {city_name}. Exception: {e}")
            return "N/A"

        return code
