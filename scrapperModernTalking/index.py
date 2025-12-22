import requests
import fake_useragent
import time
import os
print(os.getcwd())

url='https://parsinger.ru/video_downloads/videoplayback.mp4'
dc = 'D:\\'
response = requests.get(url=url, stream=True)
with open(dc + 'mt.mp4', 'wb') as file:
    file.write(response.content)
    print(os.path.getsize(dc + 'mt.mp4') / 1000000)

