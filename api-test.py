import requests

BASE = 'https://api.twilio.com/'
VERSION = '2010-04-01/'
API = BASE + VERSION

ACCOUNT_SID = 'ACaffc70db2a2f99b053bb455ba14694ef'
TOKEN = 'e05065ed11100e24a8b8ddd24aac7f4c'
NUMBER = '+16572066509'

def sendMessage(to_number, body):

	URL = API + 'Accounts/' + ACCOUNT_SID + '/Messages.json'

	payload = {
		'From': NUMBER,
		'TO': to_number,
		'Body': body
		}

r = request.post(URL, data = payload, auth = (ACCOUNT_SID,TOKEN))
print(r)

sendMessage('+19513392208', 'Hello, from diy iot')


