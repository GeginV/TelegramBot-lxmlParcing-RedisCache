import requests
import json

r = requests.get('https://baconipsum.com/api/?type=meat-and-filler')
print(r)

r = json.loads(r.content)
print(r[0])
