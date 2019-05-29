import requests
from pprint import pprint

localhost = 'http://127.0.0.1:8000'

response = requests.get(f'{localhost}/knockknock')
print(response.status_code)
print(response.text)

print()

response = requests.get(f'{localhost}/books')
print(response.status_code)
pprint(response.json())

print()

response = requests.get(f'{localhost}/books/9b30d321-d242-444f-b2db-884d04a4d806')
print(response.status_code)
pprint(response.json())

print()

response = requests.post(f'{localhost}/books', json=    
	{
        'title': 'Perfect Testing',
        'sub_title': None,
        'author': 'Gerald Weiner',
        'publisher': 'House Publishing',
        'year': 2019,
        'pages': 50
    })
print(response.status_code)
print(response.text)

print()

response = requests.post(f'{localhost}/token/joep')
print(response.status_code)
print(response.text)