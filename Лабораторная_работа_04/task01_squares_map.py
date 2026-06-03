"""Задание 1: квадраты чисел 1-10 с map."""


def squares_1_to_10() -> list[int]:
    return list(map(lambda number: number**2, range(1, 11)))


if __name__ == "__main__":
    print(squares_1_to_10())
