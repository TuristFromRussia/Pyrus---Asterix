from dataclasses import dataclass
from datetime import datetime


@dataclass
class Interaction:

    id: int | None

    client_id: int

    source: str

    external_id: str

    created_at: datetime