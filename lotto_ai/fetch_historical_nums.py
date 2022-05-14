import requests
import json

url = 'https://data.ny.gov/resource/d6yy-54nr.json'
r = requests.get(url, allow_redirects=True)
json_object = json.loads(r.content)

for i in json_object:    
    print(i)