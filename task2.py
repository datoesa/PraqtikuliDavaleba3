import requests
from pprint import pprint

data = {"color": "red", "model": "Avalon", "company": "Toyota", "price": "36 00$"}

response = requests.post('https://httpbin.org/post', data=data)

response_json = response.json()

pprint(response_json)
