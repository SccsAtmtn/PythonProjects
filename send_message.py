from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC0cbe059deef625efe1550493ba4b6501"
auth_token  = "00e624bb844fe0fb4df9902114b2eb20"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="Hello, Zhitao!",
    to="+8617710305576",    # Replace with your phone number
    from_="+12017629261 ") # Replace with your Twilio number
print(message.sid)
