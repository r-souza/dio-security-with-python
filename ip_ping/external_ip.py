import re
import json
from urllib.request import urlopen

uri = 'http://ip-api.com/json/'

response = urlopen(uri)

data = json.load(response)

ip = data['query']
org = data['org']
city = data['city']
region = data['region']
country = data['country']

print(ip)
print(org)
print(city)
print(region)
print(country)
