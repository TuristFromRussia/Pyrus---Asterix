from dataclasses import dataclass


@dataclass
class Task:

    id: int | None

    external_id: int

    title: str

    status: str