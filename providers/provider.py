from abc import abstractmethod, ABC


class Provider(ABC):
    name: str
    key: str
    stable: bool = True

    @abstractmethod
    def get_latest_version(self) -> str:
        pass

    def print_version(self):
        print(self.name + ' -> ' + self.get_latest_version())

    @classmethod
    def all_subclasses(cls):
        """Retourne récursivement toutes les sous-classes concrètes et sélectionnables
        (non abstraites, avec un attribut `key` propre) de Provider."""
        result = []
        for subclass in cls.__subclasses__():
            if not getattr(subclass, "__abstractmethods__", None) and "key" in vars(subclass):
                result.append(subclass)
            result.extend(subclass.all_subclasses())
        return result
