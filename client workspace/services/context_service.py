from domain.client_context import (
    ClientContext
)

from repositories.client_repository import (
    ClientRepository
)

from repositories.call_repository import (
    CallRepository
)


class ContextService:

    def __init__(
        self,
        client_repository,
        call_repository
    ):

        self.client_repo = (
            client_repository
        )

        self.call_repo = (
            call_repository
        )

    def get_context_by_phone(
        self,
        phone: str
        ) -> ClientContext | None:

        client = (
            self.client_repo
            .get_by_phone(phone)
        )

        if not client:
            return None

        calls = (
            self.call_repo
            .get_by_client_id(client.id)
        )

        return ClientContext(
            client=client,
            active_tasks=[],
            recent_calls=calls,
            interactions=[]
        )