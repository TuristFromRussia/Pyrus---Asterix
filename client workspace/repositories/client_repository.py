from domain.client import Client
from storage.db import get_connection


class ClientRepository:

    def create(
        self,
        phone: str,
        name: str | None = None,
        company: str | None = None
    ) -> Client:

        conn = get_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO clients
            (
                phone,
                name,
                company
            )
            VALUES (?, ?, ?)
            """,
            (
                phone,
                name,
                company
            )
        )

        conn.commit()

        client_id = cursor.lastrowid

        conn.close()

        return Client(
            id=client_id,
            phone=phone,
            name=name,
            company=company
        )
    
    # получение телефона клиента из БД


    def get_by_phone(
        self,
        phone: str
    ) -> Client | None:

        conn = get_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM clients
            WHERE phone = ?
            """,
            (phone,)
        )

        row = cursor.fetchone()

        conn.close()

        if row is None:
            return None

        return Client(
            id=row["id"],
            phone=row["phone"],
            name=row["name"],
            company=row["company"]
        )

    # получение всех данных о клиенте из БД
    def get_all(self) -> list[Client]:

        conn = get_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM clients
            ORDER BY id
            """
        )

        rows = cursor.fetchall()

        conn.close()

        result = []

        for row in rows:

            result.append(
                Client(
                    id=row["id"],
                    phone=row["phone"],
                    name=row["name"],
                    company=row["company"]
                )
            )

        return result