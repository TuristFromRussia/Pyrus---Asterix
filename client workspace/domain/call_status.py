from enum import Enum


class CallStatus(str, Enum):

    NEW = "new"

    RINGING = "ringing"

    ANSWERED = "answered"

    COMPLETED = "completed"

    MISSED = "missed"

    FAILED = "failed"