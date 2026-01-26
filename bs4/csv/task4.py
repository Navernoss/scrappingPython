import csv
import requests
from bs4 import BeautifulSoup as bs

with open ('res.csv','w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file,delimiter=';')
    writer.writerow(["Наименование", "Артикул", "Бренд", "Модель", "Тип", "Технология экрана", "Материал корпуса", "Материал браслета", "Размер", "Сайт производителя", "Наличие", "Цена", "Старая цена", "Ссылка на карточку с товаром"])

url_prime = 'https://parsinger.ru/html/index1_page_1.html'
flatten =[]
response_prime = requests.get(url=url_prime)
response_prime.encoding = 'utf-8'
soup_prime = bs(response_prime.text,'lxml')
count_of_pages = int(soup_prime.find('div', class_="pagen").find_all('a')[-1].text)
count_of_categories = len(soup_prime.find('div',class_="nav_menu").find_all('a'))

last_links = []
for xxx in range(1, int(count_of_categories)+ 1):
    for i in range(1,int(count_of_pages) + 1):
        url = f'https://parsinger.ru/html/index{xxx}_page_{i}.html'
        response = requests.get(url=url)
        response.encoding = 'utf-8'
        soup = bs(response.text,'lxml')
        links = [x['href'] for x in soup.find_all('a', class_='name_item')]
        last_links += links
 
last_links = [f'https://parsinger.ru/html/{link}' for link in last_links]
for link in last_links:
    url = link
    response = requests.get(url=url)
    response.encoding = 'utf-8'
    soup = bs(response.text,'lxml')
    name = soup.find('p',id="p_header").text
    price = soup.find('span',id="price").text
    description = [d.text.strip() for d in soup.find('ul', id="description").find_all('li')]
    old_price = soup.find('span',id="old_price").text
    count = soup.find('span',id="in_stock").text
    article = soup.find('p',class_="article").text
    inf = [name,article.split(':')[1].strip(),*[desc.split(':')[1].strip() for desc in description if desc],count.split(':')[1].strip(),price,old_price,link]
    flatten.append(inf)

with open ('res.csv','a', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file,delimiter=';')
    writer.writerows(flatten)
file.close()

