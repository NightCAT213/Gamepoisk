from bs4 import BeautifulSoup
import requests

res = requests.get('https://playmodapp.ru/logical/4809-skazki-i-golovolomki-dlya-detey.html')
soup = BeautifulSoup(res.text, 'lxml')
a = str(soup.find_all('div', class_="p_content"))
a = a.split('<br/>')[0][29:]
print(a)

