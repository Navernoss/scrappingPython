from bs4 import BeautifulSoup
import requests

url = 'https://parsinger.ru/html/index1_page_1.html'

response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
pagen = soup.find('div', class_='pagen').find_all('a')[-1]
print(pagen)
# pagen = [link['href'] for link in pagen]
# schema = "https://parsinger.ru/html"
# pagen = [schema + link for link in pagen]
# # print(pagen)

# # Генерация ссылок

# url_list = []
# for x in range(1,10):
#     url_list.append(f'https://parsinger.ru/html/index1_page_{x}.html')
# print(url_list)