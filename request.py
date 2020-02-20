import requests as rq

url = "http://www.google.com"

response = rq.get(url)

print(f"your reques to {url} came with status {response.status_code}")