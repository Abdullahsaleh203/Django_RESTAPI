import requests

endpoint ="https://httpbin.org/status/200/"
endpoint ="https://httpbin.org/anything"

response = requests.get(endpoint,json={"query":
"hello world"})   # => HTTP [GET] request to the endpoint api
# response = requests.get(endpoint,json={"query":"hello world"})   # => GET request to the endpoint api
print(response.text)         # => print raw  text response


# HTTP Response -> HTML
# REST API  HTTP Request -> JSON
print(response.json())         # 
