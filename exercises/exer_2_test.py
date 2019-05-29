import requests

localhost = 'http://127.0.0.1:8000'

def test_knock():
		response = requests.get(f'{localhost}/knockknock')
		assert response.status_code == 200
		assert response.text == "Who's there?"

def test_get_books():
		response = requests.get(f'{localhost}/books')
		assert response.status_code == 200
		assert response.status_code < 400
		assert len(response.json()) != 0

def test_get_one_book():
		id = '9b30d321-d242-444f-b2db-884d04a4d806'
		response = requests.get(f'{localhost}/books/{id}')
		assert response.status_code == 200
		assert response.status_code < 400
		assert response.json() == {
															'author': 'Gerald Weinberg',
														  'id': '9b30d321-d242-444f-b2db-884d04a4d806',
														  'pages': 182,
														  'publisher': 'Dorset House Publishing',
														  'sub_title': None,
														  'title': 'Perfect Software And Other Illusions About Testing',
														  'year': 2008}
		data = response.json()
		assert data['sub_title'] == None

def test_post_book():
		response = requests.post(f'{localhost}/books', json=    
																												{
																											        'title': 'Perfect Testing',
																											        'sub_title': None,
																											        'author': 'Gerald Weiner',
																											        'publisher': 'House Publishing',
																											        'year': 2019,
																											        'pages': 50
																											    })
		assert response.status_code == 201
		assert len(response.json()) != 0

def test_post_book_fails():
		response = requests.post(f'{localhost}/books', json=    
																												{
																															#'title' is missing
																											        'sub_title': None,
																											        'author': 'Gerald Weiner',
																											        'publisher': 'House Publishing',
																											        'year': 2019,
																											        'pages': 50
																											    })
		assert response.status_code == 400

def test_get_token():
		user = 'joep'
		response = requests.post(f'{localhost}/token/{user}')
		assert response.status_code == 201
		# data = response.json()
		# assert len(data['token']) != 0
		assert len(response.json()) != 0



