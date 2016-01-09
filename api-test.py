import requests

BASE = 'https://api.twilio.com/'
VERSION = '2010-04-01/'
API = BASE + VERSION

ACCOUNT_SID = 'AC639b11fb2dbbe5e6416a104a51d55c07'
TOKEN = '3817c55f21fc7c3bd075d061be13c7fd'
NUMBER = '+19513392208'

def sendMessage(to_number, body):

	URL = API + 'Accounts/' + ACCOUNT_SID + '/Messages.json'

	payload = {
		'From': NUMBER,
		'TO': to_number,
		'Body': body
		}

	r = requests.post(URL, data = payload, auth = (ACCOUNT_SID,TOKEN))
	print(r)

sendMessage('+16572066509', 'Hello, from diy iot')
