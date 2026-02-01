import requests
from bs4 import BeautifulSoup
import json
url = 'https://parsinger.ru/html/index1_page_1.html'

response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text,'lxml')
count_of_categories = len(soup.find('div', class_='nav_menu').find_all('a'))
result_json = []
for x in range(1,count_of_categories):
    url = f'https://parsinger.ru/html/index{x}_page_1.html'
    response = requests.get(url=url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text,'lxml')
    count_of_pages = len(soup.find('div', class_="pagen").find_all('a'))
    for y in range(1,count_of_pages + 1):
        url_pages = f'https://parsinger.ru/html/index{x}_page_{y}.html'
        response_pages = requests.get(url=url_pages)
        response_pages.encoding = 'utf-8'
        soup_pages = BeautifulSoup(response_pages.text,'lxml')
        list_of_links = [f'https://parsinger.ru/html/{link['href']}' for link in soup_pages.find_all('a', class_='name_item')]
        names = [name.text.strip() for name in soup_pages.find_all('a', class_='name_item')]
        description = [desc.text.split('\n') for desc in soup_pages.find_all('div', class_="description")]
        prices = [name.text.strip() for name in soup_pages.find_all('div', class_="price_box")]
        for i in range(0, len(names)):
            flatten = [str(names[i]), *[d.split(':')[1].strip() for d in description[i] if d], prices[i]]
            if x == 1:
                result_json.append({
                    'name': flatten[0],
                    'brand': flatten[1],
                    'type': flatten[2],
                    'material': flatten[3],
                    'display': flatten[4],
                    'price': flatten[5]
                })
            elif x == 2:
                result_json.append({
                    'name': flatten[0],
                    'brand': flatten[1],
                    'diagonal': flatten[2],
                    'material': flatten[3],
                    'resolution': flatten[4],
                    'price': flatten[5]
                })
            elif x == 3:
                result_json.append({
                    'name': flatten[0],
                    'brand': flatten[1],
                    'type': flatten[2],
                    'connect': flatten[3],
                    'game': flatten[4],
                    'price': flatten[5]
                })
            elif x == 4:
                result_json.append({
                    'name': flatten[0],
                    'brand': flatten[1],
                    'form-factor': flatten[2],
                    'capacity': flatten[3],
                    'buffer-memory': flatten[4],
                    'price': flatten[5]
                })
            elif x == 5:
                result_json.append({
                    'name': flatten[0],
                    'brand': flatten[1],
                    'type of connect': flatten[2],
                    'color': flatten[3],
                    'type of headphones': flatten[4],
                    'price': flatten[5]
                })
with open ('res.json','w', encoding='utf-8-sig') as file:
    json.dump(result_json,file,indent=4,ensure_ascii=False)
