from services.call_service import (
    CallService
)

service = CallService()

call = service.process_incoming_call(
    phone="+79991112233",
    unique_id="111111",
    linked_id="111111"
)

print(call)

service.complete_call(
    "111111"
)