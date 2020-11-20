import requests
import os
from dotenv import load_dotenv

load_dotenv('./discord_py_env')
TOKEN = os.getenv('COINBASE_TOKEN')

def get_spot_price(koin):
	url = f"https://api.coinbase.com/v2/prices/{koin}-USD/spot"
	headers = {'Authorization': f"Bearer {TOKEN}"}
	try:
		raw_data = requests.get(url, headers=headers)
		koin_data = raw_data.json()
		spot_price = str(koin_data['data']['amount'])
		return f"The current spot price of {koin} is ${spot_price}."
	except KeyError as e:
		print(e)
		return "Pick a real cryptocurrency you jackass!"
