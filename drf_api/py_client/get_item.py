import requests
from getpass import getpass
from drf_api.server_config import PORT

username = input("Login: ")
password = getpass("Password: ")

token_gen_endpoint = f"http://localhost:{PORT}/api/auth/"
auth_response = requests.post(token_gen_endpoint, json={"username": username, "password": password})
print(auth_response.json())
if auth_response.status_code == 200:
    token = auth_response.json()["token"]
    endpoint = f"http://localhost:{PORT}/api/products/"
    headers = {
        "Authorization": f"Token {token}"
    }
    response = requests.get(endpoint, headers=headers)
    print(response.json())
