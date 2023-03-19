from bs4 import BeautifulSoup
import requests

res = requests.get('https://tv.yandex.ru/channel/sts-8')
soup = BeautifulSoup(res.text, 'lxml')
print(soup.find("a", class_= "link channel-schedule__link"))
