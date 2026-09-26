import requests

from .provider import Provider

class GradleProvider(Provider):
    name = "gradle"
    key = "gradle"

    def get_latest_version(self) -> str:
        response = requests.get(
            "https://services.gradle.org/versions/current",
            timeout=5,
        )
        response.raise_for_status()
        data = response.json()
        return data["version"]