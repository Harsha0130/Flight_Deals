import requests
# from pprint import pprint

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/f72c7dde575b917aa0ceee138a8b92fd/flightDeals/prices"
SHEETY_USERS_ENDPOINT = "https://api.sheety.co/f72c7dde575b917aa0ceee138a8b92fd/flightDeals/users"
header = {
    "Authorization": "Basic SGFyc2hhOktha2thQDEyMw=="
}


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}
        self.customer_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=header)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_code(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}", headers=header, json=new_data)
            print(response.text)

    def get_customer_emails(self):
        response = requests.get(url=SHEETY_USERS_ENDPOINT, headers=header)
        data = response.json()
        print(data)
        self.customer_data = data["users"]
        return self.customer_data
