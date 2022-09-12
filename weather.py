from urllib import request, response
import requests

API_KEY = "dcb2b92ff42ec75f7493945c932068e4"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data["weather"][0]["description"]
    temperature = round(data["main"]["temp"] - 273.15, 2)

    print(f"Weather: {weather}")
    print(f"Temperature: {temperature}°C")
else:
    print("An error occurred.")