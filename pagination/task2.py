from bs4 import BeautifulSoup
import requests

url = 'https://parsinger.ru/html/index3_page_1.html'
response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
pagen = soup.find('div', class_='pagen').find_all('a')
pagen = [link['href'] for link in pagen]
schema = "https://parsinger.ru/html/"
pagen = [schema + link for link in pagen]
sum = 0
main_list = []
for x in range(0,len(pagen)):
    urls = f'{pagen[x]}'
    response1 = requests.get(url=urls)
    response1.encoding = 'utf-8'
    soup1 = BeautifulSoup(response1.text, 'lxml')
    name_list = soup1.find_all(class_="name_item")
    for y in range(0,len(name_list)):
        name_list[y] = name_list[y]['href']
    for z in range(0,len(name_list)):
        urlz = f'{schema}{name_list[z]}'
        print(urlz)
        response2 = requests.get(url=urlz)
        response2.encoding = 'utf-8'
        soup2 = BeautifulSoup(response2.text, 'lxml')
        article = int(soup2.find('p', class_='article').text.replace('Артикул: ',''))
        sum += article
print(sum)
