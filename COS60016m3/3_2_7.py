import requests

requests.get(
    'https://samples.openweathermap.org/data/2.5/',
    params=[('q', 'Chicago, USA')],
)

print(requests.get)

import requests

query = {'q': 'stream', 'order': 'length', 'min_width': '5000', 'min_height': '300'}
req = requests.get('https://flickr.com/en/photos/', params=query)

print(req.url)