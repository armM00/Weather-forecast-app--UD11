#  api.json of www.openweathermap.org

import requests
import json

API_KEY = "YOUR_API_KEY"


def get_data(place, forecast_days):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    request = requests.get(url)
    response = request.json()
    filtered_data = response['list']
    number_values = 8 * forecast_days  # each day contains info of 8 checks. checks are made every 3 hours. 8 checks/day
    filtered_data = filtered_data[:number_values]
    return filtered_data


if __name__ == '__main__':
    print(get_data(place='Tokyo', forecast_days=1))
