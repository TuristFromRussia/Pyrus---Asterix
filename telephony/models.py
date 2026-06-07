from dataclasses import dataclass
from datetime import datetime

# Заполняется звонок в итоге.
@dataclass
class Call:

    unique_id: str

    linked_id: str

    caller_number: str

    destination_number: str

    started_at: datetime

    ended_at: datetime | None = None

    recording_file: str | None = None

    status: str = "ringing"