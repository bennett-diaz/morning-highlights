from twilio.rest import Client
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")
RECEIVER_PHONE_NUMBER = os.getenv("RECEIVER_PHONE_NUMBER")

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)


def send_sms(msg):
    try:
        client.messages.create(
            body=msg,
            from_=TWILIO_PHONE_NUMBER,
            to=RECEIVER_PHONE_NUMBER,
        )
    except TwilioError as te:
        print(f"Exception: There was a Twilio error in send_sms(): {te}")


if __name__ == "__main__":
    print("You are only running" + __file__ + "and not importing it.")
