import requests

# endpoint = 'https://httpbin.org/anything'
endpoint = 'http://localhost:8000/api/products/1/update/'

data = {
    'title':'Hello World Updated!!',
    'price': 125.05,
}

get_response = requests.put(endpoint, json=data)
# print(get_response.text)
# print(get_response.status_code)
print(get_response.json())