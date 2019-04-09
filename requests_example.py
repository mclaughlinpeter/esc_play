import requests

url = 'https://samples.openweathermap.org/data/2.5/weather?q=London,uk&appid=b6907d289e10d714a6e88b30761fae22'
response = requests.get(url)
print("status code: ", response.status_code)

response_dictionary = response.json()

print(response_dictionary.keys())
print("temp in London: ", response_dictionary['main']['temp'])