import requests as re

url = 'http://127.0.0.1:8000/api/v1/mebel_sayt/ctg/'


def get_list(token, ):
    import requests

    url = "http://127.0.0.1:8000/api/v1/mebel_sayt/ctg/"

    payload = {}
    headers = {
        'Authorization': f'Bearer {token}'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return response.json()
