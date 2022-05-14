from twilio.rest import Client
import os

from dotenv import load_dotenv

load_dotenv()

account_sid = os.getenv('account_sid')
auth_token = os.getenv('auth_token')
# client = Client(account_sid, auth_token) 
print(account_sid, auth_token)
def sendMessage(client, body):
    # print(message.sid)
    pass