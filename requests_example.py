# https://openweathermap.org/

import requests

url = 'https://samples.openweathermap.org/data/2.5/weather?q=London,uk&appid=b6907d289e10d714a6e88b30761fae22'

response = requests.get(url)

response_dictionary = response.json()

print("Temperature in London: ", response_dictionary['main']['temp'])