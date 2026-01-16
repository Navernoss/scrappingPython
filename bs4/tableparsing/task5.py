import requests
from bs4 import BeautifulSoup

url = 'https://parsinger.ru/table/5/index.html'

responce = requests.get(url=url)
soup = BeautifulSoup(responce.text, 'lxml')
unic_digit = soup.find_all(class_ = 'orange')
all_digits = soup.find_all('td')
path = 14
sum = 0
while path < len(all_digits):
    it = float(unic_digit[int(path/15)].text) * float(all_digits[path].text)
    print(f'{float(unic_digit[int(path/15)].text)} * {float(all_digits[path].text)}')
    sum += it
    path += 15
print(sum)
