import requests
import json
import jsonpath

url = "https://reqres.in/api/users?page=2"

res = requests.get(url)
json_response = json.loads(res.text)

#print(res.headers)
#print(res.content)
print(json_response)

pages = jsonpath.jsonpath(json_response,"total_pages")

print(pages)

