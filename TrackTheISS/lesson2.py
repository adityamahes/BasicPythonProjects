# API Parameters
# Allows you to give an input for making API request. Gives you the specific data that you wnt
# How you do that is said in the API documentation
# Like a function there are default and required arguments

import requests
from datetime import datetime
LOCAL_UTC_OFFSET = -4


def utc_to_local(utc_hour):
    utc_hour += LOCAL_UTC_OFFSET
    if LOCAL_UTC_OFFSET > 0:
        if utc_hour > 23:
            utc_hour -= 24
    elif LOCAL_UTC_OFFSET < 0:
        if utc_hour < 0:
            utc_hour += 24
    return utc_hour


# We can do :
parameters = {
    "lat": 43.502480,  # Required
    "lng": -80.180330,  # Required... the others are not required
    "formatted": 0,
}
# 1.
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)

# 2.
# response = requests.get(f"https://api.sunrise-sunset.org/json?lat={parameters['lat']}&lng={parameters['lng']}")
# response.raise_for_status()
response.raise_for_status()
data = response.json()
sunrise = utc_to_local(int(data["results"]["sunrise"].split("T")[1].split(":")[0]))
sunset = utc_to_local(int(data["results"]["sunset"].split("T")[1].split(":")[0]))
time_now = datetime.now()
print(sunrise)
print(sunset)
print(time_now.hour)