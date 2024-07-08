import requests


class DataManager:
    # This class is responsible for talking to the Google Sheet.

    sheety_api_endpoint = "https://api.sheety.co/f72c7dde575b917aa0ceee138a8b92fd/flightDeals/prices"

    header1 = {
        "Authorization": "Basic SGFyc2hhOktha2thQDEyMw=="
    }
