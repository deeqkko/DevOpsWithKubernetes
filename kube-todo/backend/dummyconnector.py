import requests
import os
import json

url = os.getenv('DUMMY_URL', default="http://localhost:8085")

def get_dummy_tasks():
    try:
        req_content = requests.get(url).content
        data = req_content.decode("utf-8")
        data = json.loads(data)
    except:
        data = {'task':['no connection...']}
    
    return data