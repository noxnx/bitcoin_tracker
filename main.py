import requests

response = requests.get('https://api.coinbase.com/v2/exchange-rates?currency=BTC')
response.raise_for_status()

data = response.json()
btc_eur = data["data"]["rates"]["EUR"]
print(btc_eur)