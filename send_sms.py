from twilio.rest import Client
import os

def send_text(message,phone_num):
    client = Client(os.environ['twilio_sid'], os.environ['twilio_auth_token'])

    client.messages.create(to=phone_num,
                           from_="+1 7655713456",
                           body=message)