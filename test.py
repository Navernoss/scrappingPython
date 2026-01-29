import requests 
from bs4 import BeautifulSoup

url = 'https://solght.ru/about/teachers/pedagogicheskiy-sostav/ankushina-marina-teodorovna/'

response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text,'lxml')
name = soup.find('div',class_="col-md-4 left-column").find('div',class_="class=col-md-8")
print(soup)