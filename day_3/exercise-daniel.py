import requests
import json

# using the requests package, we can make API calls to retrieve JSON
# and storing it into a variable here called "response"
response = requests.get("https://rickandmortyapi.com/api/character")

# verify the response status as 200
# print(response)

# verify the raw string data of the response
# print(response.text)

# load as a python json object and store into a variable called "clean_data"
clean_data = json.loads(response.text)

print(clean_data)

# go through the results,

# for each row in an excel spreadsheet
# grab the name, species, gender, location name