from datetime import datetime

from domain.call import Call
from domain.call_status import CallStatus

from storage.db import get_connection


class CallRepository:
# По сути создаем хранилище звонков
# первый метод create создает в бд сам звонок
    def create(
        self,
        call: Call
    ) -> Call:

        conn = get_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO calls
            (
                client_id,
                unique_id,
                linked_id,
                status,
                started_at,
                ended_at
            )
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                call.client_id,
                call.unique_id,
                call.linked_id,
                call.status.value,
                call.started_at.isoformat(),
                call.ended_at.isoformat()
                if call.ended_at
                else None
            )
        )

        conn.commit()

        call.id = cursor.lastrowid

        conn.close()

        return call
    

# выборка id звонков 

    def get_by_unique_id(
        self,
        unique_id: str
    ) -> Call | None:

        conn = get_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM calls
            WHERE unique_id = ?
            """,
            (unique_id,)
        )

        row = cursor.fetchone()

        conn.close()

        if row is None:
            return None

        return Call(
            id=row["id"],
            client_id=row["client_id"],
            unique_id=row["unique_id"],
            linked_id=row["linked_id"],
            status=CallStatus(
                row["status"]
            ),
            started_at=datetime.fromisoformat(
                row["started_at"]
            ),
            ended_at=(
                datetime.fromisoformat(
                    row["ended_at"]
                )
                if row["ended_at"]
                else None
            )
        )

# статус звонка по его id

    def update_status(
        self,
        unique_id: str,
        status: CallStatus
    ):

        conn = get_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            UPDATE calls
            SET status = ?
            WHERE unique_id = ?
            """,
            (
                status.value,
                unique_id
            )
        )

        conn.commit()

        conn.close()



# получение id клиента
    def get_by_client_id(
        self,
        client_id: int
    ) -> list[Call]:

        conn = get_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM calls
            WHERE client_id = ?
            ORDER BY started_at DESC
            """,
            (client_id,)
        )

        rows = cursor.fetchall()

        conn.close()

        result = []

        for row in rows:

            result.append(
                Call(
                    id=row["id"],
                    client_id=row["client_id"],
                    unique_id=row["unique_id"],
                    linked_id=row["linked_id"],
                    status=CallStatus(
                        row["status"]
                    ),
                    started_at=datetime.fromisoformat(
                        row["started_at"]
                    ),
                    ended_at=(
                        datetime.fromisoformat(
                            row["ended_at"]
                        )
                        if row["ended_at"]
                        else None
                    )
                )
            )

        return result