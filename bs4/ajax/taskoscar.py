import requests

url = 'https://www.scrapethissite.com/pages/ajax-javascript/?'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:146.0) Gecko/20100101 Firefox/146.0',
    'X-Requested-With': 'XMLHttpRequest',
}

year = input('Введите год (2010-2015): ')

params = {
    'ajax':'true',
    'year': year
}

responce = requests.get(url=url, headers=headers, params=params).json()
print(f'Фильмы {year} года: \n')

for item in responce:
    print(f'{item['title']}')
