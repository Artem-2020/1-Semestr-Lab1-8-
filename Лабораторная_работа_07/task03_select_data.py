"""Задание 3: выбрать данные из таблицы."""

import sqlite3
from pathlib import Path


DB_PATH = Path(__file__).with_name("library.db")


def prepare_database(connection: sqlite3.Connection) -> None:
    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL
        )
        """
    )
    connection.execute("DELETE FROM books")
    connection.execute("DELETE FROM sqlite_sequence WHERE name = 'books'")
    connection.executemany(
        "INSERT INTO books (title, author) VALUES (?, ?)",
        [
            ("Изучаем Python", "Лутц"),
            ("Программируем на Python", "Доусон"),
            ("Python и анализ данных", "Маккинни"),
        ],
    )
    connection.commit()


def main() -> None:
    with sqlite3.connect(DB_PATH) as connection:
        connection.row_factory = sqlite3.Row
        prepare_database(connection)
        rows = connection.execute("SELECT id, title, author FROM books ORDER BY id").fetchall()

    for row in rows:
        print(f"{row['id']}. {row['title']} - {row['author']}")


if __name__ == "__main__":
    main()
