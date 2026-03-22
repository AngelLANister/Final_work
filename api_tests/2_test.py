import requests
from dotenv import load_dotenv
load_dotenv()
import os

def test_get_film():
    token = os.getenv('token')
    base_url_for_api = os.getenv('base_url_for_api')
    headers_auth = {'Content-Type':
                        'application/json',
                    'x-api-key': token}
    resp_get_film = requests.get(base_url_for_api +
                                        '/v1.4/movie/1183582',
                                    headers=headers_auth)
    data = resp_get_film.json()
    assert data["name"] == "Холоп"
    assert resp_get_film.status_code == 200
