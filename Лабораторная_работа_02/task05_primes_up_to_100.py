"""Задание 5: список простых чисел до 100."""


def primes_up_to(limit: int) -> list[int]:
    primes: list[int] = []
    for number in range(2, limit + 1):
        is_prime = True
        for divisor in range(2, int(number**0.5) + 1):
            if number % divisor == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(number)
    return primes


if __name__ == "__main__":
    print(primes_up_to(100))
