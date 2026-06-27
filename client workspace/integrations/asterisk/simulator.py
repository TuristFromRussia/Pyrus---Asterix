from uuid import uuid4


class AsteriskSimulator:
    def __init__(
    self,
    call_service
):
        self.call_service = (
            call_service
    )
        
    def simulate_call(
        self,
        phone: str
    ):

        unique_id = str(
            uuid4()
        )

        self.call_service.process_incoming_call(
            phone=phone,
            unique_id=unique_id,
            linked_id=unique_id
        )