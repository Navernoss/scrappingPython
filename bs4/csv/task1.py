import csv
import requests
from bs4 import BeautifulSoup as bs

with open ('res.csv','w',encoding='utf-8-sig',newline='') as file:
    writer = csv.writer(file,delimiter=';')
    writer.writerow(['Наименование', 'Бренд', 'Форм фактор','Ёмкость', 'Объём буф памяти', 'Цена'])

urlp = 'https://parsinger.ru/html/index4_page_1.html'
responsep = requests.get(url=urlp)
responsep.encoding='utf-8'
soupp = bs(responsep.text,'lxml')
countofpages = soupp.find('div',class_='pagen').find_all('a')[-1].text
flatten=[]
for x in range(1,int(countofpages)+1):
    url = f'https://parsinger.ru/html/index4_page_{x}.html'
    
    response = requests.get(url=url)
    response.encoding='utf-8'
    soup = bs(response.text,'lxml')
    name = [x.text.strip() for x in soup.find_all(class_='name_item')]
    desc = [x.text.split('\n') for x in soup.find_all('div',class_='description')]
    price = [x.text.strip() for x in soup.find_all('p',class_="price")]
    
    for i in range(0,len(name)):
        flatten.append([name[i],*[x.split(':')[1].strip() for x in desc[i] if x],price[i]])

with open('res.csv','a',encoding='utf-8-sig',newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerows(flatten)
file.close()