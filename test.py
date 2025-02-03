import pytest
from main import get_github_user, get_weather
from config import apikey

def test_get_github_user(mocker):
    mock_get = mocker.patch('main.requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        'login': 'nizavr',
        'id': 345178,
        'name': 'Ivan'
    }

    user_data = get_github_user('nizavr')

    assert user_data == {
        'login': 'nizavr',
        'id': 345178,
        'name': 'Ivan'
    }

def test_get_github_user_with_error(mocker):
    mock_get = mocker.patch('main.requests.get')
    mock_get.return_value.status_code = 500

    user_data = get_github_user('nizavr')

    assert user_data == None

def test_get_weather(mocker):
    mock_get = mocker.patch('main.requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        'weather': [{'description': 'clear sky'}],
        'main': {'temp': 273.15}
    }

    city = 'London'

    weather_data = get_weather(apikey, city)

    assert weather_data == {
        'weather': [{'description': 'clear sky'}],
        'main': {'temp': 273.15}
    }

def test_get_weather_with_error(mocker):
    mock_get = mocker.patch('main.requests.get')
    mock_get.return_value.status_code = 404

    city = 'London'

    weather_data = get_weather(apikey, city)

    assert weather_data == None

