from bs4 import BeautifulSoup
import requests

url = 'https://parsinger.ru/html/index1_page_1.html'
responce = requests.get(url=url)
responce.encoding = 'utf-8'
soup = BeautifulSoup(responce.text, 'lxml')
div = soup.find('div', 'item').find_all('li')
for txt in div:
        print(txt.text)


"""
Объяснение кода:

responce.encoding = 'utf-8' - строка написанная дабы не получать непонятных символов, при парсинге страниц
soup = BeautifulSoup(responce.text, 'lxml') = строка увлажняющая спаршенную дату, без нее код имеет множество пробелов
.find('div', 'item') -  ищет одно совпадение div с классом ite,
.find_all('li') - ищет все li теги и создает из них массив. Текст можно извлечь методом .text
for txt in div:
        print(txt.text)

"""