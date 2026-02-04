import requests 
from bs4 import BeautifulSoup

url = 'https://solght.ru/about/teachers/pedagogicheskiy-sostav/antipina-mariya-vladimirovna/'

response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text,'lxml')
name = soup.find('div',class_="wp-section").find('div',class_="row").find('div',class_="col-md-8").find('h1').text
print(name)