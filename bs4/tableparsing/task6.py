import requests
from bs4 import BeautifulSoup as bs

url = 'https://parsinger.ru/table/5/index.html'

response = requests.get(url=url)
soup = bs(response.text,'lxml')
all_columns = soup.find('tr').find_all('th')
all_columns = [colunm.text for colunm in all_columns]
all_rows = soup.find_all('td')
count_rows = soup.find_all('tr')
path = 0
result = {}
for x in range(0,len(all_columns)):
    sum = 0
    path = x
    while path < len(all_rows):
        sum += float(all_rows[path].text)
        path += 15
    result[f'{all_columns[x]}'] = f'{round(sum,3)}'
    
print(result)