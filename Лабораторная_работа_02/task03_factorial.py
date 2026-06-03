"""Задание 3: факториал числа."""


def factorial(number: int) -> int:
    if number < 0:
        raise ValueError("Факториал определен только для неотрицательных чисел.")

    result = 1
    for value in range(2, number + 1):
        result *= value
    return result


if __name__ == "__main__":
    number = 7
    print(f"{number}! = {factorial(number)}")
