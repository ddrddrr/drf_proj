import requests
from drf_api.server_config import PORT

endpoint = f"http://localhost:{PORT}/api/"
response = requests.post(endpoint,
                         params={"bebra": "ponychana", "aboba": "najdena"},
                         json={"title": "harry ebanyj potter", "price": 228})
print(response.json())

