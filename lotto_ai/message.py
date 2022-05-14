from twilio.rest import Client
import os

from dotenv import load_dotenv

load_dotenv()

account_sid = os.getenv('account_sid')
auth_token = os.getenv('auth_token')
client = Client(account_sid, auth_token)


def send_message(body, to_num):
    client.messages.create(
        to=to_num,
        from_=os.getenv('from_number'),
        body=body
    )
