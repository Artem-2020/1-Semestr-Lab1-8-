"""Задание 5: наследование Animal -> Dog."""


class Animal:
    def __init__(self, name: str) -> None:
        self.name = name

    def speak(self) -> str:
        return "Животное издает звук."


class Dog(Animal):
    def speak(self) -> str:
        return f"{self.name} говорит: Гав!"


if __name__ == "__main__":
    dog = Dog("Шарик")
    print(dog.speak())
