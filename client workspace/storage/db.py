import sqlite3
from pathlib import Path

def get_connection():
    # Находим папку, где лежит db.py (storage), и берем её родителя (client workspace)
    db_path = Path(__file__).resolve().parent.parent / "workspace.db"
    
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn