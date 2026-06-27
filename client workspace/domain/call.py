from dataclasses import dataclass
from datetime import datetime

from domain.call_status import CallStatus


@dataclass
class Call:

    id: int | None

    client_id: int

    unique_id: str

    linked_id: str

    status: CallStatus

    started_at: datetime

    ended_at: datetime | None = None