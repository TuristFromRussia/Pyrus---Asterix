from domain.client import Client

from repositories.client_repository import (
    ClientRepository
)


class ClientService:

    def __init__(
        self,
        client_repository: ClientRepository
    ):

        self.client_repo = client_repository

    def get_or_create_client(
        self,
        phone: str
    ) -> Client:

        client = (
            self.client_repo
            .get_by_phone(phone)
        )

        if client:
            return client

        return self.client_repo.create(
            phone=phone
        )