import requests

# endpoint = 'https://httpbin.org/anything'
endpoint = 'http://localhost:8000/api/products/'

data = {
    'title':'Create Field test',
}

get_response = requests.post(endpoint, json=data)
# print(get_response.text)
# print(get_response.status_code)
print(get_response.json())