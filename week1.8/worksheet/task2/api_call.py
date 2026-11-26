
import httpx

base_url = "https://dummyjson.com/products/search?phone"


content=""

url = base_url + content  # API request

response = httpx.get(url)   # API call

print(response.status_code)   # HTTP response

content = response.json()   # JSON data

print(content)





    

