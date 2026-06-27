from datetime import datetime

from repositories.call_repository import (
    CallRepository
)

from domain.call import Call
from domain.call_status import (
    CallStatus
)


repo = CallRepository()

call = Call(
    id=None,
    client_id=1,
    unique_id="123456",
    linked_id="123456",
    status=CallStatus.RINGING,
    started_at=datetime.now()
)

repo.create(call)

saved = repo.get_by_unique_id(
    "123456"
)

print(saved)

repo.update_status(
    "123456",
    CallStatus.COMPLETED
)

saved = repo.get_by_unique_id(
    "123456"
)

print(saved)