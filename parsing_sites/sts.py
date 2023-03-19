from bs4 import BeautifulSoup
import requests

res = requests.get('https://kanobu.ru/games/popular/')
soup = BeautifulSoup(res.text, 'lxml')
print(soup.select_one('[class^="BaseElementCard_body__fcrUh"]'))
