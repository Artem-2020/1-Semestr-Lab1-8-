"""Задание 1: класс Book с полями title и author."""

from dataclasses import dataclass


@dataclass
class Book:
    title: str
    author: str

    def info(self) -> str:
        return f"Книга: {self.title}, автор: {self.author}"


if __name__ == "__main__":
    book = Book("Программирование на Python", "Марк Лутц")
    print(book.info())
