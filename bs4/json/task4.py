import requests
from bs4 import BeautifulSoup
import json

url_p = 'https://parsinger.ru/html/index1_page_1.html'

response_p = requests.get(url=url_p)
response_p.encoding='utf-8'
soup = BeautifulSoup(response_p.text,'lxml')
count_of_cat = len(soup.find('div',class_="nav_menu").find_all('a'))
count_of_pages = len(soup.find('div',class_="pagen").find_all('a'))
list_of_links = []
for i in range(1, count_of_cat + 1):
    for x in range(1, count_of_pages + 1):
        url = f'https://parsinger.ru/html/index{i}_page_{x}.html'
        response = requests.get(url=url)
        response.encoding='utf-8'
        soup  = BeautifulSoup(response.text,'lxml')
        links = [f'https://parsinger.ru/html/{link['href']}' for link in soup.find_all('a', class_="name_item")]
        list_of_links.extend(links)
print(list_of_links)
result_json = []
for link in list_of_links:
    url = link
    response = requests.get(url=url)
    response.encoding='utf-8'
    soup = BeautifulSoup(response.text,'lxml')
    name = soup.find('p', id="p_header").text
    article = soup.find('p',class_="article").text.split(':')[1].strip()
    price = soup.find('span',id="price").text
    old_price = soup.find('span',id="old_price").text
    count = soup.find('span',id="in_stock").text.split(':')[1].strip()
    li_id = [li['id'] for li in soup.find('ul',id="description").find_all('li')]
    li_txt = [li.text.split(':')[1].strip() for li in soup.find('ul',id="description").find_all('li')]
    result_json.append({
        'name':name,
        'article': article,
        li_id[0]:li_txt[0],
        li_id[1]:li_txt[1],
        li_id[2]:li_txt[2],
        li_id[3]:li_txt[3],
        li_id[4]:li_txt[4],
        li_id[5]:li_txt[5],
        li_id[6]:li_txt[6],
        li_id[7]:li_txt[7],
        'in_stock': count,
        'price': price,
        'old_price':old_price
    })
with open('res.json','w',encoding='utf-8-sig') as file:
    json.dump(result_json,file, indent=4,ensure_ascii=False)
print('Операция завершена')