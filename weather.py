import requests


def Weather(city):
    api_key = "3c0b20a112faaef8c985d24ead334665"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    final_url = base_url + "appid=" + api_key + "&q=" + city + "&units=metric"
    weather_data = requests.get(final_url).json()
    return weather_data['main']
