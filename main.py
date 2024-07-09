# This file will need to use the DataManager,FlightSearch, FlightData,
# NotificationManager classes to achieve the program requirements.
import time
from data_manager import DataManager
from flight_search import FlightSearch

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
print(sheet_data)

flight_search = FlightSearch()

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
        time.sleep(2)
    print(f"sheet_data:\n {sheet_data}")

    print("Updated sheet data with IATA codes:")
    print(sheet_data)

    data_manager.destination_data = sheet_data
    data_manager.update_destination_code()
