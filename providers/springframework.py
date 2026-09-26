from .maven_artifact_provider import MavenArtifactProvider

class SpringProvider(MavenArtifactProvider):
    name = "Spring Framework"
    key = "spring"
    group_id = "org.springframework"
    artifact_id = "spring-core"