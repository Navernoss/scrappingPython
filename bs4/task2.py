# 1. Открываем сайт
# 2. Получаем данные при помощи bs4 о старой цене и новой цене
# 3. По формуле высчитываем процент скидки
# 4. Формула: (старая цена - новая цена) * 100 / старая цена
# 5. Вставьте получившийся результат в поле ответа
# 6. Ответ должен быть числом с 1 знаком после запятой.

from bs4 import BeautifulSoup
import requests

url = 'https://parsinger.ru/html/hdd/4/4_1.html'

response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
old = soup.find('span',id='old_price').text
new = soup.find('span',id='price').text
new = int(new.replace(' руб', ''))
old = int(old.replace(' руб', ''))
discount = (old - new) * 100 / old
print(round(discount,1))