import requests


ENDPOINT = "https://opentdb.com/api.php"
response = requests.get(url=ENDPOINT, params={"amount": 10, "difficulty": "medium", "type": "boolean"})
response.raise_for_status()
data = response.json()

question_data = data["results"]
print(len(question_data))