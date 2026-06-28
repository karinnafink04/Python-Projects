import requests
import os
import time
from win11toast import toast


with open('weather_api.txt', 'r') as file:
    api = file.read()
    
url = 'https://api.openweathermap.org/data/2.5/weather'
parameters = {"lat": 38.405963, 'lon': -78.713965, 'appid': api, 'units': 'metric'}

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
