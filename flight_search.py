import requests
import os

AMADEUS_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"
AMADEUS_API_KEY = os.environ["AMADEUS_API_KEY"]
AMADEUS_API_SECRET = os.environ["AMADEUS_API_SECRET"]


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def get_destination_code(self, city_name):
        code = "TESTING"
        return code
