import requests

API_KEY = "d7087f427ea2ae654d1f427xyzxyzxyzxyz"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather" # the target URL to hit.

# paramters:
city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"