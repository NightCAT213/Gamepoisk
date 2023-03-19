import requests

json_data = [11849]

res = requests.post('https://www.wildberries.ru/webapi/poo/byids', json=json_data)
print(res)
a = res.json()
print('рейтинг', a['value']['11849']['rate'])
