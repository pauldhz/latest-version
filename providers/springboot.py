from .maven_artifact_provider import MavenArtifactProvider

class SpringBootProvider(MavenArtifactProvider):
    name = "Spring Boot"
    key = "springboot"
    group_id = "org.springframework.boot"
    artifact_id = "spring-boot"