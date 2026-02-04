import requests
from bs4 import BeautifulSoup
import json
import time
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
result_json = []
url_p = 'https://parsinger.ru/html/index3_page_1.html'
response_p = requests.get(url=url_p, timeout=5 ,headers=headers)
soup_p = BeautifulSoup(response_p.text,'lxml')
count_of_pages = int(len(soup_p.find('div',class_='pagen').find_all('a')))
list_of_links = []
time.sleep(5)
for i in range(1,count_of_pages + 1):
    url = f'https://parsinger.ru/html/index3_page_{i}.html'
    response = requests.get(url=url, timeout=10, headers=headers)
    soup = BeautifulSoup(response.text,'lxml')
    links_of_page = [f'https://parsinger.ru/html/{link['href']}' for link in soup.find_all('a',class_='name_item')]
    list_of_links.extend(links_of_page)
    time.sleep(5)
for link in list_of_links:
    url = link
    
    response = requests.get(url=url, timeout=20, headers=headers)
    response.encoding='utf-8'
    soup = BeautifulSoup(response.text,'lxml')
    name = soup.find('p',id="p_header").text
    article = soup.find('p', class_='article')
    description = soup.find('ul', id='description').find_all('li')
    in_stock = soup.find('span', id='in_stock').text.split(':')[1].strip()
    price = soup.find('span',id="price").text.split(' ')[0].strip()
    li_id = [x['id'] for x in description]
    li_text = [x.text.split(':')[1].strip() for x in description]
    li_id.extend(article['class'])
    result_json.append({
        'name':name,
        li_id[-1]:article.text,
        li_id[0]:li_text[0],
        li_id[1]:li_text[1],
        li_id[2]:li_text[2],
        li_id[3]:li_text[3],
        li_id[4]:li_text[4],
        li_id[5]:li_text[5],
        li_id[6]:li_text[6],
        li_id[7]:li_text[7],
        'in_stock': in_stock,
        'price': price
    })
    time.sleep(3)

with open ('res.json','w',encoding='utf-8-sig') as file:
    json.dump(result_json,file,indent=4, ensure_ascii=False)