
import sqlite3
from pathlib import Path
from datetime import datetime



BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "data" / "search_history.db"


def get_connection():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)

    return sqlite3.connect(DB_PATH)


def initialize_history():
    with get_connection() as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS search_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                query TEXT NOT NULL,
                budget REAL,
                category TEXT,
                searched_at TEXT NOT NULL
            )
        """)


def save_search(query, budget=None, category=None):
    initialize_history()

    with get_connection() as connection:
        connection.execute(
            """
            INSERT INTO search_history
            (query, budget, category, searched_at)
            VALUES (?, ?, ?, ?)
            """,
            (
                query.strip(),
                budget,
                category,
                datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            )
        )


def get_search_history(limit=100):
    initialize_history()

    with get_connection() as connection:
        cursor = connection.execute(
            """
            SELECT id, query, budget, category, searched_at
            FROM search_history
            ORDER BY id DESC
            LIMIT ?
            """,
            (limit,)
        )

        return cursor.fetchall()


def clear_search_history():
    initialize_history()

    with get_connection() as connection:
        connection.execute("DELETE FROM search_history")
