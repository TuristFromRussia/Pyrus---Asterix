from datetime import datetime
from telephony.models import Call
from telephony.call_manager import CallManager
from telephony.ami_client import FakeAMIClient


manager = CallManager()

ami = FakeAMIClient()

event = ami.simulate_call()

call = Call(
    unique_id=event.unique_id,
    linked_id=event.linked_id,
    caller_number=event.caller,
    destination_number=event.destination,
    started_at=datetime.now()
)

manager.on_new_call(call)

manager.on_hangup(event.unique_id)