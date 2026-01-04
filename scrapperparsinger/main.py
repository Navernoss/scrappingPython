from bs4 import BeautifulSoup
import requests

url = 'https://parsinger.ru/html/watch/1/1_1.html'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Referer': 'www.google.com'
}

responce = requests.get(url=url, headers=headers)
responce.encoding='utf-8'
soup = BeautifulSoup(responce.text,'lxml')
name = soup.find('p', id ='p_header').text
article = soup.find('p', class_='article').text
description = soup.find('ul', id='description').find_all('li')
count = soup.find('span', id='in_stock').text
price = soup.find('span', id='price').text
old_price=soup.find('span', id='old_price').text
# print()




print(f'Название: {name}\n{article}\n{count}\nНовая цена: {price}\nСтарая цена: {old_price}')
for txt in description:
    print(txt.text)

# Happy birthday)