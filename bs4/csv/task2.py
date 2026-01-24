import csv
import requests
from bs4 import BeautifulSoup as bs

url_prime = 'https://parsinger.ru/html/index1_page_1.html'

response_prime = requests.get(url=url_prime)
response_prime.encoding = 'utf-8'
soup_prime = bs(response_prime.text,'lxml')
count_of_pages = soup_prime.find('div', class_="pagen").find_all('a')[-1].text
last = []
for i in range(1,int(count_of_pages) + 1):
    url = f'https://parsinger.ru/html/index1_page_{i}.html'
    response = requests.get(url=url)
    response.encoding = 'utf-8'
    soup = bs(response.text,'lxml')
    names_list = [name.text.strip() for name in soup.find_all('a', class_="name_item")]
    
    prices_list = [price.text.strip() for price in soup.find_all('p', class_="price")]
    descriptions_list = [desc.text.split('\n') for desc in soup.find_all('div',class_="description")]
    # print(descriptions_list)
    # print('-----\n')
    for x in range(0, len(names_list)):
        last.append([names_list[x],*[y.split(':')[1].strip() for y in descriptions_list[x] if y], prices_list[x]])

with open('res.csv', 'w',newline='',encoding='utf-8-sig') as file:
    writer = csv.writer(file,delimiter=';')
    writer.writerows(last)
file.close()