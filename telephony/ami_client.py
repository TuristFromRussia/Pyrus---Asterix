import uuid

from telephony.events import (
    NewCallEvent,
    HangupEvent
)

# Пока что здесь фейковая ответка от ami, потому что нет постоянного доступа. 
# Здесь мы получаем инфу по звонку от астерикса
class FakeAMIClient:

    def simulate_call(self):

        uid = str(uuid.uuid4())

        return NewCallEvent(
            unique_id=uid,
            linked_id=uid,
            caller="+79991234567",
            destination="101"
        )

    def simulate_hangup(self, uid):

        return HangupEvent(
            unique_id=uid
        )