# Открываем сайт
# Извлекаем при помощи bs4 данные о стоимости часов (всего 8 шт)
# Складываем все числа
# Вставляем результат в поле ответа

from bs4 import BeautifulSoup
import requests

url = 'https://parsinger.ru/html/index1_page_1.html'

response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
all_prices = soup.findAll(class_='price')
sum = 0
for price in all_prices:
    sum += int(price.text.replace(' руб', ''))
print(sum)
