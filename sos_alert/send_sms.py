# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
def send_alert(name, sender, receiver):
    account_sid = 'AC3a179cf2762ab7ac90d01cc71ad3ab6b'
    auth_token = '8a0f8c0232868cf9e2f6771a6e5ce366'
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body=f"SOS Alert\n{name} is in danger",
                        from_=f'{sender}',
                        to=f'{receiver}'
                    )

    print(message.sid)