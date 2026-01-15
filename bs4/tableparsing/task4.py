import requests
from bs4 import BeautifulSoup

url = 'https://parsinger.ru/table/4/index.html'

response = requests.get(url=url)
soup = BeautifulSoup(response.text,'lxml') 
all_green = soup.find_all(class_='green')
sum = 0
for green in all_green:
    sum += float(green.text)
print(sum)                                                                        