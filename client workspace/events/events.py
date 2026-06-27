from dataclasses import dataclass
from datetime import datetime


@dataclass
class Event:

    occurred_at: datetime



@dataclass
class CallStartedEvent:

    phone: str

    unique_id: str

    linked_id: str

    occurred_at: datetime



@dataclass
class CallCompletedEvent:

    unique_id: str

    occurred_at: datetime