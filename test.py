import pytest
from main import get_catapi, get_github_user, get_weather
from config import apikey

def test_get_catapi(mocker):
    mock_get = mocker.patch('main.requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        'id': 'b9u',
        'url': 'https://cdn2.thecatapi.com/images/b9u.jpg',
        'width': 500,
        'height': 333
    }
    cat = get_catapi()
    assert cat == {
        'id': 'b9u',
        'url': 'https://cdn2.thecatapi.com/images/b9u.jpg',
        'width': 500,
        'height': 333
    }

def test_get_catapi_with_error(mocker):
    mock_get = mocker.patch('main.requests.get')
    mock_get.return_value.status_code = 404
    cat = get_catapi()
    assert cat == None

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
