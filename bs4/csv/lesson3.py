import csv
import requests
from bs4 import BeautifulSoup

with open('res.csv','w',newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file,delimiter=';')
    writer.writerow(['Наименование','Цена','Бренд','Тип','Подключение','Игровая'])

url = "https://parsinger.ru/html/index3_page_2.html"

response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')

name = [x.text.strip() for x in soup.find_all('a', class_ = 'name_item')]
description = [x.text.split('\n') for x in soup.find_all('div',class_='description')]
price = [x.text for x in soup.find_all('p', class_='price')]

for item,price,descr in zip(name,price,description):
    flatten = item, price, *[x.split(':')[1].strip() for x in descr if x]
    file = open('res.csv', 'a',encoding='utf-8-sig', newline='')
    writer = csv.writer(file,delimiter=';')
    writer.writerow(flatten)
file.close()