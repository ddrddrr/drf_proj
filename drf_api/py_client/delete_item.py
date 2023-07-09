import requests
from drf_api.server_config import PORT

item_id = 3
endpoint = f"http://localhost:{PORT}/api/products/{item_id}/delete/"
response = requests.delete(endpoint)
print(response.status_code)
