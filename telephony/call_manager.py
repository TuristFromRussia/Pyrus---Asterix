from telephony.models import Call

# По сути обработчик звонка и создатель выходных данных
class CallManager:

    def __init__(self):

        self.active_calls: dict[str, Call] = {}

    def on_new_call(self, call: Call):

        self.active_calls[call.unique_id] = call

        print(
            f"NEW CALL: "
            f"{call.caller_number} -> {call.destination_number}"
        )

    def on_hangup(self, unique_id: str):

        call = self.active_calls.get(unique_id)

        if not call:
            return

        call.status = "completed"

        print(
            f"CALL ENDED: "
            f"{call.caller_number}"
        )   