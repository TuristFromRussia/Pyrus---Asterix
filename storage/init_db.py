from db import get_connection


def create_tables():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS calls (
            id INTEGER PRIMARY KEY AUTOINCREMENT,

            unique_id TEXT NOT NULL,
            linked_id TEXT NOT NULL,

            caller_number TEXT NOT NULL,
            destination_number TEXT,

            status TEXT NOT NULL,

            started_at TEXT NOT NULL,
            ended_at TEXT
        )
    """)

    conn.commit()

    conn.close()