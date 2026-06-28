# api key: 5b77b04104e1431b41aa99a44768bee8

import requests
import os
import time
from win11toast import toast

url = 'https://api.openweathermap.org/data/2.5/weather'
parameters = {"lat": 38.405963, 'lon': -78.713965, 'appid': '5b77b04104e1431b41aa99a44768bee8', 'units': 'metric'}

response = requests.get(url, params = parameters, timeout=10)
data = response.json()

description  = data["weather"][0]["description"].capitalize()


while True:
    response = requests.get(url, params = parameters, timeout=10)
    data = response.json()

    new_description  = data["weather"][0]["description"].capitalize()
    
    if (new_description != description):
        toast('Weather Update', new_description)
        description = new_description
        
    time.sleep(60)
    
