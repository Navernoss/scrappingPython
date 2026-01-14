import requests
from bs4 import BeautifulSoup

url = 'https://parsinger.ru/table/2/index.html'

response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text,'lxml')
list_column = soup.find_all('th')
all_digits = soup.find_all('td')
path = 0
sum = 0
while path < len(all_digits):
    sum += float(all_digits[path].text)
    path += 15
print(sum)