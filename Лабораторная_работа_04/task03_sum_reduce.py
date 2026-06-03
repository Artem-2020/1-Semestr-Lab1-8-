"""Задание 3: сумма чисел через reduce."""

from functools import reduce
from typing import Iterable


def sum_with_reduce(numbers: Iterable[int]) -> int:
    return reduce(lambda total, number: total + number, numbers, 0)


if __name__ == "__main__":
    print(sum_with_reduce([4, 8, 15, 16, 23, 42]))
