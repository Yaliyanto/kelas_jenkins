import requests

BASE_URL = 'https://api-test.kelasotomesyen.com'

# TOKEN
def get_token():
  payload_get_token = {
    "email": "pyautoid@gmail.com",
    "password": "1234567890"
  }

  param = {"grant_type": "password"}

  resp_get_token = requests.post(url=f'{BASE_URL}/auth/v1/token', json=payload_get_token, params=param)
  response_json = resp_get_token.json()
  token = response_json['access_token']
  
  return token

token = get_token()
header_api = {
    'apikey':'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im50dWZ4ZnFvbWhta3Vnc3F0eWdtIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjM2MjU2MTIsImV4cCI6MjA3OTIwMTYxMn0.rK59L5TG51fQmPeAkXT_yOzGWWyUcJbK4jgw-nCIC9Q',
    'Authorization': f'Bearer {token}'
  }
# GET

def get_user():
  resp_get_userid = requests.get(f'{BASE_URL}/auth/v1/user', headers=header_api)
  data_user = resp_get_userid.json()
  user_id = data_user['id']
  return user_id


# POST
def test_post_product():
  user_id = get_user()
  payload_post_product = {
    "name": "Laptop Gaming",
    "description": "High performance gaming laptop",
    "price": 15000000,
    "stock": 10,
    "category": "Electronics",
    "user_id": f"{user_id}",
  }

  response_post_product = requests.post(f'{BASE_URL}/rest/v1/products', headers=header_api, json=payload_post_product)
  assert response_post_product.status_code == 201

def test_get_product():
  response_get_product = requests.get(f'{BASE_URL}/rest/v1/products',headers=header_api)
  
  assert response_get_product.status_code == 200
  assert response_get_product.json()[0]['name'] == 'Laptop Gaming'
  
# # GET
# def get_product_id():
#   response_get_product = requests.get(f'{BASE_URL}/rest/v1/products',headers=header_api)
#   id_product = response_get_product.json()[0]['id']
#   return id_product


# # DELETE
# def test_delete():
#   id_product = get_product_id()
#   param_product = {'id':f'eq.{id_product}'}
#   response_delete_product = requests.delete(f'{BASE_URL}/rest/v1/products',headers=header_api, params=param_product)
#   assert response_delete_product.status_code == 204
  