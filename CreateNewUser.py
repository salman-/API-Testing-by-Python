import requests
import json
import jsonpath
import os

script_dir = os.path.dirname(__file__) # absolute dir the script is in
rel_path = '/jsons/CreateNewUser'
abs_file_path = script_dir+ rel_path
request = open(abs_file_path,'r').read()

url = "https://reqres.in/api/users"
request_json = json.loads(request)
response = requests.post(url,request_json)
res = json.loads(response.text)
id = jsonpath.jsonpath(res,"id")

print(request)
print(response.content)
print(id[0])