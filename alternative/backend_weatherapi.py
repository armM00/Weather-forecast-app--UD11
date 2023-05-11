#  api.json of www.weatherapi.com

import requests
import json


with open('api.json') as file:
    key = json.load(file)

API_KEY = key["weatherapi"]


def get_data(place, forecast_days):
    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={place}&days={forecast_days}&aqi=yes&alerts=no"
    request = requests.get(url)
    response = request.json()
    return response
