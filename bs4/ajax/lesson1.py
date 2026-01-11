import requests

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'x-requested-with':'XMLHttpRequest'
}

url = 'https://bitality.cc/Home/GetSum?GiveName=Bitcoin&GetName=Ether Classic&Sum=0.25&Direction=0'
responce = requests.get(url=url, headers=headers).json()
print(responce)