import requests

# endpoint = 'https://httpbin.org/anything'
endpoint = 'http://localhost:8000/api/'
get_response = requests.post(endpoint, json={'title':'Hello world POST!!','content':'Another Amazing Product','price':'123'})
# print(get_response.text)
# print(get_response.status_code)
print(get_response.json())