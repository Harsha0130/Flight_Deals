from twilio.rest import Client
import os

ACCOUNT_SID = os.environ["ACCOUNT_SID"]
AUTH_TOKEN = os.environ["AUTH_TOKEN"]
TWILIO_NUMBER = os.environ["TWILIO_NUMBER"]
MY_NUMBER = os.environ["MY_NUMBER"]


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details
    def __init__(self):
        self.client = Client(ACCOUNT_SID, AUTH_TOKEN)

    def send_whatsapp(self, message_body):
        message = self.client.messages.create(
            from_=f'whatsapp:{TWILIO_NUMBER}',
            body=message_body,
            to=f'whatsapp:{MY_NUMBER}'
        )
        # Prints if successfully sent.
        print(message.sid)
