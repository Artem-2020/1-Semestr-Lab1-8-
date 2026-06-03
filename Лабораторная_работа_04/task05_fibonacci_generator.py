"""Задание 5: генератор Фибоначчи."""

from typing import Iterator


def fibonacci(count: int) -> Iterator[int]:
    first, second = 0, 1
    for _ in range(count):
        yield first
        first, second = second, first + second


if __name__ == "__main__":
    print(list(fibonacci(12)))
