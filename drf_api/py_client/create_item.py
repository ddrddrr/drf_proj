import requests
from drf_api.server_config import PORT
from random import randint

payload1 = {"title": f"moby giant dick{randint(1, 100)}",
            "price": randint(0, 5000)}
payload2 = {"title": f"moby with a lesser one {randint(1, 100)}",
            "content": "same, but sadder story as a moby dick",
            "price": randint(0, 5000)}
endpoint = f"http://localhost:{PORT}/api/products/"

response = requests.post(endpoint, payload1)
print(response.json())
response = requests.post(endpoint, payload2)
print(response.json())
