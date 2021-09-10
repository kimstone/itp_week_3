import requests
import json
import openpyxl
from openpyxl.styles import fonts

response = requests.get("https://rickandmortyapi.com/api/character")

# print(response)
# print(response.text)

clean_data = json.loads(response.text)

# print(clean_data)
print(type(clean_data))

# go through the results for each row in an excel spreadsheet
# grab the name, species, gender,  and location name

# ws1 = my_new_workbook.create_sheet("Sheet1")

for x in clean_data:
    #print(x)
    if x == "results":
        for i in clean_data["results"]:
            print(str(i['id']) + ' : ' + i['name'] + ' : ' + i['species'] + ' : ' + i['gender'] + ' : ' + i['location']['name'])
            #print(type(i['gender']))
            #print(type(i['location']))

# char['location']['name']

filename = "/Users/techmate/Training/ViT/PythonDataScience/itp_week_3/day_3/output.xlsx"
wb = openpyxl.load_workbook(filename)

sheet = wb['Sheet1']

sheet['A1'] = "Name"
#sheet['A1'].font = Font(bold = True)
sheet['B1'] = "Species"
sheet['C1'] = "Gender"
sheet['D1'] = "Location"

counter = 2

result = clean_data["results"]

for char in result:
    print(char['name'])
    sheet['A' + str(counter)] = char['name']
    sheet['B' + str(counter)] = char['species']
    sheet['C' + str(counter)] = char['gender']
    sheet['D' + str(counter)] = char['location']['name']
    counter+=1

wb.save(filename)