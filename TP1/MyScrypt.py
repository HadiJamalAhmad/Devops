# 
import requests

longitude = input('Enter your longitude :')
latitude = input('Enter your latitude :')



import requests
import json
api_key = "e9129c74b39d7c39f4009a8cc1d371d5"
lat = str(latitude)
lon = str(longitude)
url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=metric" % (lat, lon, api_key)
response = requests.get(url)
data = json.loads(response.text)
print(data)


