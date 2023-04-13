from bs4 import BeautifulSoup
import requests

res = requests.get('https://skazbuka.com/')
soup = BeautifulSoup(res.text, 'lxml')
a = str(soup.find_all('div', class_="t480__descr t-descr t-descr_md", limit=3))
print(a)

