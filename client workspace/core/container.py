from repositories.client_repository import (
    ClientRepository
)

from repositories.call_repository import (
    CallRepository
)

from services.client_service import (
    ClientService
)

from services.call_service import (
    CallService
)

from services.context_service import (
    ContextService
)

from events.event_bus import (
    EventBus
)

from integrations.asterisk.simulator import (
    AsteriskSimulator
)

class Container:

    def __init__(self):

        self.event_bus = (
            EventBus()
        )

        self.client_repository = (
            ClientRepository()
        )

        self.client_service = (
            ClientService(
                self.client_repository
            )
        )

        self.call_repository = (
            CallRepository()
        )

        self.call_service = (
            CallService(
                self.call_repository,
                self.client_service,
                self.event_bus
            )
        )
        
        self.context_service = (
            ContextService(
                self.client_repository,
                self.call_repository
            )
        )

        self.asterisk_simulator = (
            AsteriskSimulator(
                self.call_service
            )
        )
