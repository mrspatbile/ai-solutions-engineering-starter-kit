from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True)
class FoundationRecord:
    source: str
    identifier: str
    data: dict[str, str]


class FoundationDataService(Protocol):
    def query(self, identifier: str) -> list[FoundationRecord]:
        """Return foundation-package records for a domain identifier."""


class LocalMockFoundationDataService:
    def query(self, identifier: str) -> list[FoundationRecord]:
        if not identifier.strip():
            return []
        return [
            FoundationRecord(
                source="local-mock",
                identifier=identifier,
                data={"note": "Replace with the real {{ cookiecutter.foundation_package_name }} client."},
            )
        ]


# TODO: Wrap the installed {{ cookiecutter.foundation_package_name }} package behind this Protocol.
