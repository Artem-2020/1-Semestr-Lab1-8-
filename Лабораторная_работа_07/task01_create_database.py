"""Задание 1: создать БД SQLite и таблицу."""

import sqlite3
from pathlib import Path


DB_PATH = Path(__file__).with_name("library.db")


def main() -> None:
    with sqlite3.connect(DB_PATH) as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT NOT NULL
            )
            """
        )
    print(f"База данных создана: {DB_PATH}")


if __name__ == "__main__":
    main()
