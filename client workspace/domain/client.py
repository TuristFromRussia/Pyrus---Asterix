from dataclasses import dataclass


@dataclass
class Client:

    id: int | None

    phone: str

    name: str | None = None

    company: str | None = None