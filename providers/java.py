import requests

from .provider import Provider

class JavaProvider(Provider):
    name = "java"
    key = "java"
    api_url = "https://api.adoptium.net/v3/info/available_releases"

    def get_latest_version(self) -> str:
        response = requests.get(self.api_url, timeout=5)
        response.raise_for_status()
        data = response.json()
        return str(data["most_recent_feature_release"])