import requests

from .provider import Provider


class NodeProvider(Provider):
    name = "Node.js"
    key = "node"
    api_url = "https://nodejs.org/dist/index.json"

    def get_latest_version(self) -> str:
        response = requests.get(self.api_url, timeout=5)
        response.raise_for_status()

        releases = response.json()

        return releases[0]["version"].removeprefix("v")