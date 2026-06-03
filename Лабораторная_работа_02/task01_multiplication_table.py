"""Задание 1: таблица умножения."""


def multiplication_table(size: int = 10) -> list[list[int]]:
    return [[row * col for col in range(1, size + 1)] for row in range(1, size + 1)]


def print_table(table: list[list[int]]) -> None:
    for row in table:
        print(" ".join(f"{value:3}" for value in row))


if __name__ == "__main__":
    print_table(multiplication_table())
