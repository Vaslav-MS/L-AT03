import requests
from config import apikey

def get_catapi():
    url = 'https://api.thecatapi.com/v1/images/search'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def get_github_user(username):
    url = f'https://api.github.com/users/{username}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def get_weather (apikey, city):
#   url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}'
    url = f'http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={apikey}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None
