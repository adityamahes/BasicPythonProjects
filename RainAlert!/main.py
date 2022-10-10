api_key = "d3afd16b20149161d2033e9bcad25ee9"
import requests
a = False
response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params={"lat": 43.54, "lon": 80.24, "appid=": api_key})
response.raise_for_status()
data = response.json()
for hour in data["hourly"][:11]:
    if hour["weather"][0]["id"] < 700:
        a = True

if a:
    print("RAIN BRING UMBRELLA")
