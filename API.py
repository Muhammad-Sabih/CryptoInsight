from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

#url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
#parameters = {
#  'start':'1',
#  'limit':'10',
#  'convert':'USD'
#}
#headers = {
#  'Accepts': 'application/json',
#  'X-CMC_PRO_API_KEY': 'c962eca3-8f3a-48e3-861d-12eb2e95c06c',  # Replace 'CPC_key' with your actual CoinMarketCap API key
#}

#session = Session()
#session.headers.update(headers)

#try:
#  response = session.get(url, params=parameters)
#  data = json.loads(response.text)
#  print(data)
#except (ConnectionError, Timeout, TooManyRedirects) as e:
#  print(e)


#for coin in data['data']:
#    print(f"Name: {coin['name']}")
#    print(f"Symbol: {coin['symbol']}")
#    print(f"Price: ${coin['quote']['USD']['price']}")
#    print(f"Market Cap: ${coin['quote']['USD']['market_cap']}")
#    print("-----")


class CryptoAPI:
  def __init__(self, api_key, base_url='https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'):
    """
    Initializes the CryptoAPI class with an API key and base URL.

    Parameters:
    - api_key (str): Your CoinMarketCap API key.
    - base_url (str): Base URL for the CoinMarketCap API (default provided).
    """
    self.api_key = api_key
    self.base_url = base_url
    self.session = Session()
    self.session.headers.update({
      'Accepts': 'application/json',
      'X-CMC_PRO_API_KEY': self.api_key,
    })

  def fetch_crypto_data(self, limit=10, convert='USD'):

    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
      'start': '1',
      'limit': str(limit),
      'convert': convert
    }

    try:
      response = self.session.get(url, params=parameters)
      data = json.loads(response.text)
      return data['data']
    except (ConnectionError, Timeout, TooManyRedirects) as e:
      print(f"Error fetching data: {e}")
      return None
