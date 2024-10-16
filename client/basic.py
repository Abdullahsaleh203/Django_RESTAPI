import requests

# endpoint ="https://httpbin.org/status/200/"
endpoint ="http://127.0.0.1:8000/api/"

response = requests.get(endpoint,json={"query":
"hello world"})   # => HTTP [GET] request to the endpoint api
# response = requests.get(endpoint,json={"query":"hello world"})   # => GET request to the endpoint api
print(response.text)         # => print raw  text response


# HTTP Response -> HTML
# REST API  HTTP Request -> JSON
print(response.json())         # 
print(response.status_code)         # 
