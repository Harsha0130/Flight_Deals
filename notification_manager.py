from twilio.rest import Client
import os
import smtplib

email = "r22da069@gmail.com"
password = "ghfnobsidykedygg"

ACCOUNT_SID = os.environ["ACCOUNT_SID"]
AUTH_TOKEN = os.environ["AUTH_TOKEN"]
TWILIO_NUMBER = os.environ["TWILIO_NUMBER"]
MY_NUMBER = os.environ["MY_NUMBER"]
SMTP_MY_EMAIL = os.environ["SMTP_MY_EMAIL"]
SMTP_PASSWORD = os.environ["SMTP_PASSWORD"]
SMTP_PROVIDER_EMAIL = os.environ["SMTP_PROVIDER_EMAIL"]


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details
    def __init__(self):
        self.client = Client(ACCOUNT_SID, AUTH_TOKEN)
        self.connection = smtplib.SMTP(SMTP_PROVIDER_EMAIL, 465)

    def send_whatsapp(self, message_body):
        message = self.client.messages.create(
            from_=f'whatsapp:{TWILIO_NUMBER}',
            body=message_body,
            to=f'whatsapp:{MY_NUMBER}'
        )
        # Prints if successfully sent.
        print(message.sid)

    def send_emails(self, email_list, email_body):
        with self.connection:
            self.connection.starttls()
            self.connection.login(SMTP_MY_EMAIL, SMTP_PASSWORD)
            for email in email_list:
                self.connection.sendmail(
                    from_addr=SMTP_MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{email_body}".encode('utf-8')
                )
