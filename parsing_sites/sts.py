from bs4 import BeautifulSoup
import requests

res = requests.get('https://ctc.ru/programm')
soup = BeautifulSoup(res.text, 'lxml')
print(soup.find("a", class_= "Link_link__5+N3C"))
