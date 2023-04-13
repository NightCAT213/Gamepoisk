from bs4 import BeautifulSoup
import requests

res = requests.get('https://skazbuka.com/')
soup = BeautifulSoup(res.text, 'lxml')
a = str(soup.find_all('div', class_="t480__descr t-descr t-descr_md", limit=3)).split('<div class="t480__descr '
                                                                                      't-descr t-descr_md" field="'
                                                                                      'descr" style="">')
a = a[1:]
for i in range(len(a)):
    if a[i] != a[-1]:
        a[i] = a[i][:-8]
    else:
        a[i] = a[i][:-7]
a = ' '.join(' '.join(a).split('<br/>'))
print(a)

