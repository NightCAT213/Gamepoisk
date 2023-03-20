from bs4 import BeautifulSoup
import requests

# пример запроса меток
res = requests.get('https://kanobu.ru/games/popular')
soup = BeautifulSoup(res.text, 'lxml')
a = str(soup.find_all('div', class_='knb-cell'))
games = []  # метки игры на сайте
a = a.split('href="')
a.pop(0)
for i in a:
    i = i[7:-1]
    index = i.find("/")
    games.append(i[0:index])
games = list(set(games))
print(games)

