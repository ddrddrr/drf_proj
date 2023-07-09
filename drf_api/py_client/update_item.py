import requests
from drf_api.server_config import PORT

item_id = 9
data = {"title": "smth new", "price": 228}
endpoint = f"http://localhost:{PORT}/api/products/{item_id}/update/"
response = requests.put(endpoint, json=data)
if response.status_code == 200:
    print(response.json())
