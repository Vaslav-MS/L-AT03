import requests
from config import apikey

def get_weather (apikey, city):
#   url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}'
    url = f'http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={apikey}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None


