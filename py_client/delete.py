import requests

product_id = input("Enter the product id you wannna delete")
try:
    product_id = int(product_id)
except:
    product_id=None
    print(f'{product_id} is not valid')

endpoint = f'http://localhost:8000/api/products/{product_id}/delete/'
get_response = requests.delete(endpoint)

print(get_response.status_code)