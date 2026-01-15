import requests
from bs4 import BeautifulSoup

url = 'https://parsinger.ru/table/3/index.html'

response = requests.get(url=url)
soup = BeautifulSoup(response.text,'lxml')
all_bold = soup.find_all('b')
sum = 0
for bold in all_bold:
    sum += float(bold.text)

print(f'Все жирные: {all_bold}')
print(f'Сумма: {sum}')