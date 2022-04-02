import requests


class RequestManager:
    """Класс для работы с requests"""

    def get(self, url: str, **params):
        return requests.get(url, **params)

    def post(self):
        pass

    def patch(self):
        pass

    def delete(self):
        pass
