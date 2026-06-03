"""Задание 3: класс BankAccount с пополнением и снятием."""


class BankAccount:
    def __init__(self, owner: str, balance: float = 0) -> None:
        self.owner = owner
        self._balance = balance

    @property
    def balance(self) -> float:
        return self._balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Сумма пополнения должна быть положительной.")
        self._balance += amount

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть положительной.")
        if amount > self._balance:
            raise ValueError("Недостаточно средств.")
        self._balance -= amount

    def __str__(self) -> str:
        return f"Счет владельца {self.owner}: {self.balance:.2f} руб."


if __name__ == "__main__":
    account = BankAccount("Иван", 1000)
    account.deposit(500)
    account.withdraw(300)
    print(account)
