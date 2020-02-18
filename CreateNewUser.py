import requests
import json
import jsonpath

import os
script_dir = os.path.dirname(__file__) # absolute dir the script is in
rel_path = '/jsons/CreateNewUser.json'
abs_file_path = script_dir+ rel_path

url = ""

request = open(abs_file_path,'r').read()


print(request)
#requests.post()