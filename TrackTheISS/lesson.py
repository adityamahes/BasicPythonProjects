# What are API's A set of commands, functions, protocols, and objects, that programmers can use to create software or
# interact wth an external system An interface between your program and external system. U use the rules API has
# precscribed and make a request to external system, then you will get data. API endpoint: Location of stored data (a
# URL) # When you enter URL you make a request

import requests
# Example endpoint
ENDPOINT = "http://api.open-notify.org/iss-now.json"  # Yo have to check the documentation for this.
response = requests.get(url=ENDPOINT)  # gets the data that we wat from end point
print(response)  # But we don't get response data. We get the response code.
# The most important thing response codes tell us is if the request succeeded or if it failed
# One such response cde is the 404 error, 504, etc
# If the response code:
    # 1XX: Hold on!
    # 2XX: Everything is successful
    # 3XX: You do not have permission
    # 4XX: You screwed up
    # 5XX: I screwed up (maybe server is  down)
print(response.status_code)  # You only get the response code
# What if the request fails? You can't write if statements for everysingle possibility of response codes to let the
# user know of the error
# You can:
response.raise_for_status()
data = response.json()  # To get actual data
# We can tap into it like a dictionary

print(data)
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]
iss_position = (longitude, latitude)

# We can go to latlong.net to see the location
