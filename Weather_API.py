import requests
#import json

API_KEY = "87539ae068f6242867261axxxxxxx"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather" # the target URL to hit.

# paramters:
city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)  # obviously, a GET request, to which the API will give a response

# to check the status of the "payload" (response)
if response.status_code == 200:
    data = response.json() # we'll be getting json data object back
    print(data)
else:
    print("An error occurred.")
