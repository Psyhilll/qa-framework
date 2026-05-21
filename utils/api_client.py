import requests


class APIClient:

    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()

    def get(self, endpoint, params=None):
        response = self.session.get(f"{self.base_url}{endpoint}", params=params)
        return response

    def post(self, endpoint, payload=None):
        response = self.session.post(f"{self.base_url}{endpoint}", json=payload)
        return response

    def delete(self, endpoint):
        response = self.session.delete(f"{self.base_url}{endpoint}")
        return response

    def put(self, endpoint, payload=None):
        response = self.session.put(f"{self.base_url}{endpoint}", json=payload)
        return response