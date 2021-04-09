import sys
import os
import requests

todoURL = os.getenv('todoURL')
wikiURL = os.getenv('wikiURL')

randomURL = requests.get(wikiURL).url
randomURL = 'Read: ' + randomURL

client = requests.session()

client.get(todoURL)

csrftoken = client.cookies['csrftoken']

new_task = {'task':randomURL,'csrfmiddlewaretoken':csrftoken}
headers = {'Referer': todoURL}

r = client.post(todoURL, data=new_task, headers=headers)

print(r)
print('Inserted: ' + new_task['task'])