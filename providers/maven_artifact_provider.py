import requests
import xml.etree.ElementTree as ET

from .provider import Provider

class MavenArtifactProvider(Provider):

    group_id: str
    artifact_id: str

    def get_latest_version(self) -> str:
        group_path = self.group_id.replace(".", "/")

        url = (
            f"https://repo.maven.apache.org/maven2/"
            f"{group_path}/{self.artifact_id}/"
            f"maven-metadata.xml"
        )

        response = requests.get(url, timeout=5)
        response.raise_for_status()

        root = ET.fromstring(response.text)

        version = root.findtext("./versioning/release")

        if version is None:
            raise ValueError(
                f"No release found for "
                f"{self.group_id}:{self.artifact_id}"
            )

        return version