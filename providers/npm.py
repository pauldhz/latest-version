import requests

from .provider import Provider


class NPMProvider(Provider):
    name = "npm"
    key = "npm"
    api_url = "https://registry.npmjs.org/npm"

    def get_latest_version(self) -> str:
        response = requests.get(self.api_url, timeout=5)
        response.raise_for_status()

        data = response.json()

        return data["dist-tags"]["latest"]