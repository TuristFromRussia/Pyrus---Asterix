from datetime import datetime

from domain.call import Call
from domain.call_status import CallStatus

from repositories.call_repository import (
    CallRepository
)

from services.client_service import (
    ClientService
)


from events.events import (
    CallStartedEvent
)

class CallService:

    def __init__(
        self,
        call_repository,
        client_service,
        event_bus
    ):
        self.call_repo = call_repository

        self.client_service = client_service

        self.event_bus = event_bus


    def process_incoming_call(
        self,
        phone: str,
        unique_id: str,
        linked_id: str
    ) -> Call:

        client = (
            self.client_service
            .get_or_create_client(phone)
        )

        call = Call(
            id=None,
            client_id=client.id,
            unique_id=unique_id,
            linked_id=linked_id,
            status=CallStatus.RINGING,
            started_at=datetime.now()
        )

        self.event_bus.publish(
            CallStartedEvent(
                phone=phone,
                unique_id=unique_id,
                linked_id=linked_id,
                occurred_at=datetime.now()
            )
        )

        
        return self.call_repo.create(
            call
        )


    def complete_call(
        self,
        unique_id: str
    ):

        self.call_repo.update_status(
            unique_id,
            CallStatus.COMPLETED
        )
    
