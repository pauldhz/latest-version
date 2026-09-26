import requests

from .provider import Provider

class PipProvider(Provider):
    name = "pip"
    key = "pip"

    def get_latest_version(self) -> str:
        response = requests.get("https://pypi.org/pypi/pip/json", timeout=5)
        response.raise_for_status()
        return response.json()["info"]["version"]