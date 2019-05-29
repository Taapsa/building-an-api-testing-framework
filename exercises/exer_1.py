import requests
import json
from pprint import pprint

localhost = 'http://127.0.0.1:8000'

#What's up?
response = requests.get(f'{localhost}/knockknock')
print(response.status_code)
print(response.text)

print()

#Getting all the books
response = requests.get(f'{localhost}/books')
print(response.status_code)
pprint(response.json())

print()

#Getting the book by ID
response = requests.get(f'{localhost}/books/9b30d321-d242-444f-b2db-884d04a4d806')
print(response.status_code)
pprint(response.json())

print()

#Getting the first books
response = requests.get(f'{localhost}/books')
print(response.status_code)
data = response.json()
pprint (data[0])

print()

#Posting a book
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

#Getting a token
response = requests.post(f'{localhost}/token/joep')
print(response.status_code)
print(response.text)