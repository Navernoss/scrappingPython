import requests
from bs4 import BeautifulSoup
import json

url = 'https://parsinger.ru/html/index1_page_1.html'

response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text,'lxml')
name = [x.text for x in soup.find_all(class_="name_item")]
desc = [x.text.split('\n') for x in soup.find_all(class_="description") if x]
prices = [x.text for x in soup.find_all('p', class_="price")]

result_json = []

for name, desc, price in zip(name,desc,prices):
    flatten = name, price, *[x.split(':')[1].strip() for x in desc if x]
    result_json.append({
    'name': flatten[0],
    'price': flatten[1],
    'brand': flatten[2],
    'type': flatten[3],
    'material': flatten[4],
    'screen': flatten[5],
    })
    
with open('res.json','w',encoding='utf-8-sig') as file:
    json.dump(result_json,file,indent=4, ensure_ascii=False)