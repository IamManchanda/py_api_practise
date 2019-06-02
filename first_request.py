import requests

url = "https://www.google.co.in/"
response = requests.get(url)
print(f"Your requests to {url} came back with status code {response.status_code}")

