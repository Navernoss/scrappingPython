from bs4 import BeautifulSoup
import requests

url = 'https://parsinger.ru/html/index1_page_1.html'

responsen = requests.get(url=url)
responsen.encoding = 'utf-8'
soupn = BeautifulSoup(responsen.text, 'lxml')
pagenav = soupn.find('div', class_='nav_menu').find_all('a')
pagenav = [link['href'] for link in pagenav]
schema = "https://parsinger.ru/html/"
pagenav = [schema + link for link in pagenav]
sum = 0

for x in range(0,len(pagenav)):
    urlx = f'{pagenav[x]}'
    response = requests.get(url=urlx)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    pagen = soup.find('div', class_='pagen').find_all('a')
    pagen = [link['href'] for link in pagen]
    schema = "https://parsinger.ru/html/"
    pagen = [schema + link for link in pagen]
    print(pagen)
    for y in range(0,len(pagen)):
        urly = f'{pagen[y]}'
        responsey = requests.get(url=urly)
        responsey.encoding = 'utf-8'
        soupy = BeautifulSoup(responsey.text, 'lxml')
        name_list = soupy.find_all(class_="name_item")
        for z in range(0,len(name_list)):
            name_list[z] = name_list[z]['href']
        for a in range(0, len(name_list)):
            urla = f'{schema}{name_list[a]}'
            responsea = requests.get(url=urla)
            responsea.encoding = 'utf-8'
            soupa = BeautifulSoup(responsea.text, 'lxml')
            count = int(soupa.find('span', id="in_stock").text.replace('В наличии: ', ''))
            price = int(soupa.find('span', id="price").text.replace(' руб', ''))
            sum1 = count * price
            
            sum += sum1
print(sum)