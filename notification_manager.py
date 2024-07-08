import requests
from twilio.rest import Client
import os


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.

    ACCOUNT_SID = os.environ["ACCOUNT_SID"]
    AUTH_TOKEN = os.environ["AUTH_TOKEN"]
    TWILIO_NUMBER = os.environ["TWILIO_NUMBER"]
