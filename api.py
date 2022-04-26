import requests
import json

url = "https://vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com/api/npm-covid-data/"

headers = {
	"X-RapidAPI-Host": "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com",
	"X-RapidAPI-Key": "7829d7bdf8mshcf4ce5a94347c0fp1ce785jsndd65a2a3c09b"
}

response = requests.request("GET", url, headers=headers)

# print(response.text)
response1=response.json()

with open("api.json","w") as file:
    json.dump(response1,file)

# print(response1[2]['Country'])

# print(response1['data']['confirmed'])
