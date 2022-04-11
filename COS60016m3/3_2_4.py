import requests

URL = 'https://www.google.com'
res = requests.get(url=URL)

print(res)

if res.status_code == 200:
    print(res.headers)
else:
    print(res.status_code)