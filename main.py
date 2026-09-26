import argparse
import sys

from providers import Provider


def build_registry() -> dict[str, type[Provider]]:
    """Construit dynamiquement le registre {key: classe} à partir de toutes les
    sous-classes concrètes de Provider (auto-découverte)."""
    return {cls.key: cls for cls in Provider.all_subclasses()}


def build_parser(registry: dict[str, type[Provider]]) -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="latest",
        description="Affiche la dernière version stable d'outils/langages/frameworks.",
    )
    parser.add_argument(
        "providers",
        nargs="*",
        metavar="PROVIDER",
        help=f"Providers à interroger (choix : {', '.join(sorted(registry.keys()))}). "
             f"Si aucun n'est fourni, tous les providers sont utilisés.",
    )
    parser.add_argument(
        "-a", "--all",
        action="store_true",
        help="Interroge explicitement tous les providers disponibles.",
    )
    parser.add_argument(
        "-l", "--list",
        action="store_true",
        help="Liste les providers disponibles et quitte.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    registry = build_registry()
    parser = build_parser(registry)
    args = parser.parse_args(argv)

    if args.list:
        for key in sorted(registry.keys()):
            print(key)
        return 0

    selected_keys = list(registry.keys()) if (args.all or not args.providers) else args.providers

    exit_code = 0
    for key in selected_keys:
        provider_cls = registry.get(key)
        if provider_cls is None:
            print(f"Provider inconnu : {key}", file=sys.stderr)
            exit_code = 1
            continue
        try:
            provider_cls().print_version()
        except Exception as exc:
            print(f"{provider_cls.name} -> erreur : {exc}", file=sys.stderr)
            exit_code = 1

    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
