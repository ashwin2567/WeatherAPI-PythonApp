import requests

headers = {'X-APP-TOKEN' : "f6121212f12ff12f12f1f12f1f12fa"}
payload= {'pickup_lat': 12.9490936, 'pickup_lng': 77.67773056, 'drop_lat': 12.9190934, 'drop_lng': 77.1777356, 'category': 'micro'}
response = requests.get('https://sandbox-t1.olacabs.com/v1/products', params=payload, headers=headers)
print(response.json())