
# Collecting Weather data from OpenWeather

import requests

#Make a request

latitude = 6.6018
longitude = 3.3515
API_KEY = "1f319454bc6d9370b4dc6536dbb34fd1"

weather_api = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={API_KEY}"

#Make a request
request = requests.get(url = weather_api).json()

# data collection
data = {
    'country': request ['sys']['country'],
    'city': request['name'],
    'longitude': request['coord']['lon'],
    'latitude': request['coord']['lat'],
    'temp': request['main']['temp'],
    'temp_min': request['main']['temp_min'],
    'temp_max': request['main']['temp_max'],
    'pressure' : request['main']['pressure'],
    'humidity' : request['main']['humidity'],
    'sea_level' : request['main']['sea_level'],
    'ground_level': request['main']['grnd_level'],
    'wind_speed' : request['wind']['speed'],
    'wind_degree': request['wind']['deg'],
    'sunrise': request['sys']['sunrise'],
    'sunset': request['sys']['sunset'],
    'desription': request['weather']['description'],
    }

print(data)
