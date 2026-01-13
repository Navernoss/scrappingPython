import requests
from bs4 import BeautifulSoup

url = 'https://parsinger.ru/table/1/index.html'

responce = requests.get(url=url)
responce.encoding = 'utf-8'
soup = BeautifulSoup(responce.text,'lxml')
all_digits = soup.find_all('td')
sum = 0
for digit in all_digits:
    sum += float(digit.text)
print(round(sum,2))