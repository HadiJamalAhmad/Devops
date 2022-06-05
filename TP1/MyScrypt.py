import requests
import os
import json
api_key = os.environ['API_KEY']
lat = os.environ['LAT']
lon = os.environ['LONG']
url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=metric" % (lat, lon, api_key)
response = requests.get(url)
data = json.loads(response.text)
print(data)


