from twilio.rest import TwilioRestClient

account_sid = "ACd5b96665efc7b4907da901d0858bf1f6" # Your Account SID from www.twilio.com/console
auth_token  = "daa98f27826c6c756fd7f4bb2286b5ab"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(
    body="Inch ka?",
    to="+15049099051",    # Replace with your phone number
    from_="+15045410665") # Replace with your Twilio number

print(message.sid)
