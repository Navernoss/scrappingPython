import requests
import json


url = "https://parsinger.ru/downloads/get_json/res.json"
response = requests.get(url=url).json()
cat = response[0]['categories']
res = {}
sum = 0
for item in response:
    if (item['categories'] == cat):
        print(item['categories'], item['count'])
        sum += int(item['count'])
    else:
        res[item['categories']] = sum
        sum = 0
        cat = item['categories']
print(res)