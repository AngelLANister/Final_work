import requests
from dotenv import load_dotenv
load_dotenv()
import os

def test_get_film():
    token = os.getenv('token')
    base_url_for_api = os.getenv('base_url_for_api')
    params = {
        'page': 1,
        'limit': 1,
    }
    headers_auth = {'Content-Type':
                        'application/json',
                    'x-api-key': token}
    resp_get_film = requests.get(base_url_for_api +
                                        '/v1.4/movie/search?query="Холоп"',
                                    headers=headers_auth, params=params)
    data = resp_get_film.json()
    assert data["docs"][0]["name"] == "Холоп"
    assert resp_get_film.status_code == 200
