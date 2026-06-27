from pathlib import Path

from storage.db import get_connection


def initialize_database():

    conn = get_connection()

    schema = Path(
        "storage/schema.sql"
    ).read_text(
        encoding="utf-8"
    )

    conn.executescript(schema)

    conn.commit()

    conn.close()


if __name__ == "__main__":
    initialize_database()