import requests
import os


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.

    Endpoint = "https://test.api.amadeus.com/v2/shopping/flight-offers"
    AMADEUS_API_KEY = os.environ["AMADEUS_API_KEY"]
    AMADEUS_API_SECRET = os.environ["AMADEUS_API_SECRET"]
    print(AMADEUS_API_SECRET)