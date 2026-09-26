# latest-cli

CLI in Python for getting the latest version of various software, frameworks like Java,
Gradle, Spring Boot, etc.

## Installation

### Prerequisites

- Python >= 3.10

### Exposing 'latest-cli' as a CLI tool

```bash
pip install -e .
```

### Without installation (direct execution)

```bash
pip install -r requirements.txt
python3 main.py --all
```

## Usage

```bash
latest [PROVIDER ...] [-a | --all] [-l | --list] [-h | --help]
```

### List all available providers

```bash
latest --list
```

```
gradle
java
maven
node
npm
pip
spring
springboot
```

### Query all providers

```bash
latest --all
```

or simply, with no argument (default behavior):

```bash
latest
```

Example output:

```
gradle -> 9.8.0
java -> 27
pip -> 26.2.1
Maven -> 3.9.16
Node.js -> 26.10.0
npm -> 12.1.0
Spring Boot -> 4.2.0-M2
Spring Framework -> 7.1.0-M2
```

### Query one or more specific providers

```bash
latest gradle npm
```

```
gradle -> 9.8.0
npm -> 12.1.0
```

### Help

```bash
latest --help
```

## Available providers

| Key          | Name               | Source                                        |
|--------------|--------------------|------------------------------------------------|
| `java`       | Java               | Adoptium API                                    |
| `gradle`     | Gradle             | services.gradle.org                             |
| `maven`      | Maven              | Maven Central (maven-metadata.xml)              |
| `node`       | Node.js            | nodejs.org/dist/index.json                      |
| `npm`        | npm                | registry.npmjs.org                              |
| `pip`        | pip                | PyPI                                            |
| `spring`     | Spring Framework   | Maven Central (org.springframework)             |
| `springboot` | Spring Boot        | Maven Central (org.springframework.boot)        |

## Development

Run without installation:

```bash
python3 main.py --list
python3 main.py --all
```

## License

Personal project — free to use.

