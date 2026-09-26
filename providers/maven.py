import requests
import xml.etree.ElementTree as ET

from .provider import Provider


class MavenProvider(Provider):
    name = "Maven"
    key = "maven"

    metadata_url = (
        "https://repo.maven.apache.org/maven2/"
        "org/apache/maven/maven-core/maven-metadata.xml"
    )

    def get_latest_version(self) -> str:
        response = requests.get(self.metadata_url, timeout=5)
        response.raise_for_status()

        root = ET.fromstring(response.text)

        versions = [
            version.text
            for version in root.findall("./versioning/versions/version")
            if version.text
        ]

        stable_versions = [
            version
            for version in versions
            if not self._is_prerelease(version)
        ]

        return stable_versions[-1]

    @staticmethod
    def _is_prerelease(version: str) -> bool:
        version = version.lower()

        return any(tag in version for tag in (
            "alpha",
            "beta",
            "rc",
            "snapshot",
        ))