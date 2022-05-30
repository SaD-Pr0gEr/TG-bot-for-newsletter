import requests
from requests import Response


class RequestManager:
    """Класс для работы с requests"""

    def get(self, url: str, **params) -> Response:
        return requests.get(url, **params)

    def post(self):
        pass

    def patch(self):
        pass

    def delete(self):
        pass
